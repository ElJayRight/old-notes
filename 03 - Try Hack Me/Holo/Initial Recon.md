Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Holo]]
# [Initial Recon]
## Notes
---
scope 10.200.111.0/24 and 192.168.100.0/24
192.168.100.0/24 is the internal network.

recon on 10.200.111.0/24
Two IPs are up:
10.200.111.33
10.200.111.250

10.200.111.33:
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: WordPress 5.5.3
| http-robots.txt: 21 disallowed entries (15 shown)
| /var/www/wordpress/index.php 
| /var/www/wordpress/readme.html /var/www/wordpress/wp-activate.php 
| /var/www/wordpress/wp-blog-header.php /var/www/wordpress/wp-config.php 
| /var/www/wordpress/wp-content /var/www/wordpress/wp-includes 
| /var/www/wordpress/wp-load.php /var/www/wordpress/wp-mail.php 
| /var/www/wordpress/wp-signup.php /var/www/wordpress/xmlrpc.php 
| /var/www/wordpress/license.txt /var/www/wordpress/upgrade 
|_/var/www/wordpress/wp-admin /var/www/wordpress/wp-comments-post.php
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: holo.live

33060/tcp open  mysqlx?
| fingerprint-strings: 
|   DNSStatusRequestTCP, LDAPSearchReq, NotesRPC, SSLSessionReq, TLSSessionReq, X11Probe, afp: 
|     Invalid message
|_    HY000
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
wordpress site.

HTTP title holo.live 
Wordpress version 5.5.3

Gobuster for vhosts.
www.holo.live