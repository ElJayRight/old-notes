#include <windows.h>

BOOL WINAPI DllMain(HINSTANCE hModule, DWORD Reason, LPVOID lpvReserved) {

	switch (Reason) {

	case DLL_PROCESS_ATTACH:
		MessageBox(NULL, L"VALID TEXT", L"HI!!!", MB_ICONQUESTION | MB_OK);
		break;
	}

	return TRUE;
}