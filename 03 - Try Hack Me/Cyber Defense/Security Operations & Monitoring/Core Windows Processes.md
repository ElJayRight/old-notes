# Task Manager
Can be sorted into apps and background processes.
Each task will have: Type, publisher, PID, Process name, Command line, CPU and memory
Command line equivalent is tasklist, Get-Process or ps

# System
will always have a SID of 4
can show Image Path, Parent Process, Number of Instances, User account and Start time.
Path C:\\Windows\\system32\\ntoskrnl.exe
## smss.exe
Windows session manager
User is system, running 1 process, Path of C:\\Windows\\System32 same process as system(4)
# csrss.exe
Client Server Runtime Process
Path C:\\Windows\\System32\\csrss.exe
No Parent process
User is system.
# wininit.exe
Windows initialisation process launches services.exe lsass.exe and lsaiso.exe
Path C:\\Windows\\System32\\wininit.exe
Parent process of smss.exe
## Services.exe
Service Control Manager.
Manages loading, interactive, starting and ending services.
Path C:\\Windows\\System32\\services.exe
Parent process of wininit.exe
### Svchost.exe
Service host is responsible for hosting and managing windows services. Should always have a -k parameter
Path C:\\Windows\\System32\\svchost.exe
Parent process of services.exe
# lsass.exe
Local Security Authority Subsystem Service
Path C:\\Windows\\System32\\lsass.exe
Parent process wininit.exe
# winlogon.exe
Handles the Secure Attention Sequence (CTRL+ALT+DEL)
Path C:\\Windows\\System32\\winlogon.exe
Parent process smss.exe
# explorer.exe
Path C:\\Windows\\explorer.exe
Parent Process userinit.exe