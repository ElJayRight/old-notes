IP: 10.10.11.165
## Nmap scan
3 ports open
22 ssh
80 http : apache 2.4.29 (ubuntu)
8000 http apache 2.4.38 (Debian)

Two different webservers running on two different OS's maybe docker?

Looking at 80

index.html is the landing page.
Host name: seventeen.htb

Subdomain enumeration
```bash
ffuf -u http://10.10.11.165 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H 'Host: FUZZ.seventeen.htb' -fl 533
```
exam.seventeen.htb
the page is a exam Reviewer Management System which has a sqli in exploitdb.

looking at the exploit shows the url is
```http
http://exam.seventeen.htb/?p=take_exam&id=1
```
Running sql map to dump out the users table in erms_db.
```bash
sqlmap -r req -p id --batch --threads 10 -D erms_db -T users --dump
```
the req is the file from burp when sending the above http request.
There is also a second database with two other tables that can be dumped.
db_sfms with tables user and student.

sqlmap cracked the hash for 31234: autodestruction

Checking the first dump there is reference of a oldmanagement vhost.

upload a php rev shell.
override .htaccess cause you can do that. (why is this allowed)
get shell on box which is in a docker container. Find a password for the user mark within a config file.

2020bestyearofmylife
