# Outline
Sysinternals has over 70 windows based tools which each fall into the following categories
 - File and Disk Utilities
 - Networking Utilities
 - Process Utilities
 - Security Utilities
 - System Information
 - Miscellaneous

# File and Disk Utilities
## Sigcheck
cli tool that shows file version number, timestamp information, digital signature deatils and certificate chains. You can also check the file agaisnt VirusTotal.
```powershell
sigcheck -u -e C:\Windows\System32
```
-e will scan for executable images
-u will check on virustotal.

## Streams
NTFS can provide applications with an alterante data stream to write information to.
Every file has atleast one data stream to write to, this can be used to hide information via ADS.
If this is the case there will be an additional security mesaure added to the files properties.


# Networking Utilities
## TCP View
Lets you list all the TCP and UDP endpoints on a system. Including the local and remote addresses. Using the green flag you can filter the data.


# Process Utilities
## Autoruns
This will list out all the programs that are configureed to run on boot. Checking the startup folder too.

## ProcDump
This can monitor CPU spikes and generate crash dumps during a spike.

## Process Explorer
Has two features. Can list all processes and can see DLLs that are loaded, as well as memory-mapped files.

## Process Moitor
Shows real-time file system, registry and process/thread activity. You can also capture all the events running.

## PsExec
light-weight telnet-replacement.


# Security Utilities
## Sysmon
monitors ands logs system activity to the windows event log.


# System Information
## WinObj
