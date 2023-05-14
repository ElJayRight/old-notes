# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/networked 10.10.10.146

PORT    STATE  SERVICE VERSION
22/tcp  open   ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 2275d7a74f81a7af5266e52744b1015b (RSA)
|   256 2d6328fca299c7d435b9459a4b38f9c8 (ECDSA)
|_  256 73cda05b84107da71c7c611df554cfc4 (ED25519)
80/tcp  open   http    Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).

```

## Port 80
Gobuster:
```
gobuster dir -u http://10.10.10.146 -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt
```

Finds a backup folder.