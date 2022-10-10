Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Breaching Active Directory]]

# [06 - Microsoft Deployment Toolkit]
## Notes
---
MDT and SCCM
Microsoft Deployment Toolkit (MDT) assists with automating the deployment of Microsoft OS.

PXE Boot
PXE boot is usually integrated with DHCP.
Once this is done the client will use a TFTP connection to download the PXE boot image. THsi can be exploited for two different purposes:
- Inject a privilege escalaction vector, such as a Local Admin accoutn, to agin Admin access to the OS once the PXE boot has been completed.
- Perform password scraping attacks to recover AD credentials used during the install.

Running the exploit:
Get the .bcd file and after importing PowerPXE in powershell run Get-WimFile.
Run Get-FindCredentials with the wimfile and get creds.