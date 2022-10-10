Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]]

# [Attacktive Directory]
## Notes
---
nmap scan:
```bash
PORT     STATE SERVICE       VERSION
53/tcp   open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-04-23 11:40:37Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
|   Product_Version: 10.0.17763
|_  System_Time: 2022-04-23T11:43:13+00:00
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Not valid before: 2022-04-22T11:39:29
|_Not valid after:  2022-10-22T11:39:29
|_ssl-date: 2022-04-23T11:43:28+00:00; 0s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=4/23%Time=6263E5BA%P=x86_64-pc-linux-gnu%r(DNSV
SF:ersionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\
SF:x04bind\0\0\x10\0\x03");
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2022-04-23T11:43:14
|_  start_date: N/A

```

ldap time
```bash
ldapsearch -h 10.10.90.125 -x -s base namingcontexts
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingcontexts: DC=spookysec,DC=local
namingcontexts: CN=Configuration,DC=spookysec,DC=local
namingcontexts: CN=Schema,CN=Configuration,DC=spookysec,DC=local
namingcontexts: DC=DomainDnsZones,DC=spookysec,DC=local
namingcontexts: DC=ForestDnsZones,DC=spookysec,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 2
```

Kerbrute for usernames
svc-admin looks intresting -> service account so try GetNPUsers

dumps a hash
```bash
$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:47ac46c6531dd1b3147df4972cdc0513$42676bdff4be54d0cecc636b1c2666308c3c0256389b68b868bb88c573e2c2cd9c1445e9ca8dd3202e741c392f2fbaf60e8926726e0cc4efb4f9c6e6ed62fb61352b327a20d4c13abad6ca3e0e476e1245e02802bd48e669edaf18e1e231746c36886e471eee69c3a1617f319faebcaa2701a0ecd735568211d8441e298e675095bacffba4cfeef8b5cb1873848287eec0dcdeda697c92f66c69462d9bc1e19fb4abcd09e898caec0b5191bd239941f282c00b1771005de3d68c9c59ea35cf3ce8a7715d529a4185b463bead71f11275a6e67f764bda37dff3075ae12cf83a40e251c253d5cf37563112258a85b1a2c8246c
```
management2005

smb login
find file and base64 decode
backup@spookysec.local:backup2517860

as this user you can run secretsdump and get the hash of admin
which finially has win-rm