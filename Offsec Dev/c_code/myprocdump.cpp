#include <stdio.h>
#include <windows.h>

const char* k = "[+]";
const char* e = "[-]";
const char* i = "[*]";

int main() {
	FILE* fpipe;
	DWORD PID = NULL;

	const char* command = "powershell.exe -e RwBlAHQALQBQAHIAbwBjAGUAcwBzACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGMAOgAiADEAIABzAHYAYwBoAG8AcwB0ACIAIAB8ACAAJQB7ACgAJABfACAALQBzAHAAbABpAHQAIAAiACAAIgApAFsAMwAxAF0AfQAgAHwAIABTAGUAbABlAGMAdAAtAE8AYgBqAGUAYwB0ACAALQBmAGkAcgBzAHQAIAAxAA==";
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