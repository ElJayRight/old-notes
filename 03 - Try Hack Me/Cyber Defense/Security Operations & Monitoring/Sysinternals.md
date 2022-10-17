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