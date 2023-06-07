Reference: [crow's gitbook](https://crows-nest.gitbook.io/crows-nest/malware-development/getting-started-with-malware-development)
# General Notes
## Processes
An instance of an exe. So something that holds everything to run the code. So each new chrome tab is a new process.

These can make child processes and the family of processes are blind and greedy, cant see anything and want all the processing power. 

Each process is given a Virtual Adress Space.

Three types of processes. 
- Application: GUI
- Background: Started automatically and run with no GUI (Not application and Windows then it is background)
- Windows: System level and are important. Memory management security and explorer.exe

You can give a process a priority rating:
- Realtime : It will take everything. Higher prio then IO devices.
- High
- Above Normal
- Normal : It will share.
- Below normal
- Low : Only given cpu time when no higher processes are running.

Each process will include a PID, Command line (the args given **IMPORTANT**) and path to exe.

## Threads
Each process is started with a single thread (primary / main thread). You can also give a process multiple threads. Very similar to Processes. But threads are feathers and processes are subs going mach 9 into the ground.

Will share memory, also have IDs and handles.

## Handles
Apparently exposure will teach me well enough.

generic unit of identification.

Going to be passed to other functions.

If a process finds out its process handle, window handle and module handle it can send it to a different process.

## Windows API
APIs. A waiter in a fancy food eating place (forgot the word).

Everything is backwards compatiable. So this should work on XP machines.

VERY WELL DOCUMENTED.
[READ THE DOCS](https://learn.microsoft.com/en-us/windows/win32/sysinfo/ntsetsysteminformation)

# The code bit
## MessageBox
The h prefix is just short for the data type HANDLE
```c
#include <windows.h>
  
int main(void){
  
    MessageBoxW(
        NULL,
        L"Look its a C program.",
        L"It be a box!",
        MB_OKCANCEL | MB_ICONEXCLAMATION
    );

    return EXIT_SUCCESS;

}
```

## CreateProcess
CreateProcess() != OpenProcess()
```c
#include <windows.h>
#include <stdio.h>

int main(void){
    STARTUPINFOW si;
    PROCESS_INFORMATION pi;

    if (!CreateProcessW(

        L"C:\\WINDOWS\\system32\\mspaint.exe",
        NULL,
        NULL,
        NULL,
        FALSE,
        0,
        NULL,
        NULL,
        &si,
        &pi
        
    )){
        printf("(-) failed to create process, error: %ld", GetLastError());
        return EXIT_FAILURE;
    }
    printf("(+) process started! pid: %ld", pi.dwProcessId);
    return EXIT_SUCCESS;
}
```
