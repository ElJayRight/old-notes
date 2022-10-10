Links [[00 - Global Index (Start Here!)]] [[01 - PicoGym]] [[Web Challenges]]

# [[01 - GET aHEAD]]
## Contents
***
- [Task Description](01%20-%20GET%20aHEAD.md#Task%20Description)
- [Notes](01%20-%20GET%20aHEAD.md#Notes)
- [Solve Script](01%20-%20GET%20aHEAD.md#Solve%20Script)

### Task Description
---
Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:53554/]

### Notes
---
Looking at the requests in burp to see what causes the page to change
**For red:**
``` http
GET /index.php? HTTP/1.1
Host: mercury.picoctf.net:53554
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://mercury.picoctf.net:53554/index.php
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
```
**For Blue**
```http
POST /index.php HTTP/1.1
Host: mercury.picoctf.net:53554
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Origin: http://mercury.picoctf.net:53554
Connection: close
Referer: http://mercury.picoctf.net:53554/index.php?
Upgrade-Insecure-Requests: 1
```
The thing that is changing is the request type on the first line. As the challenge is called *GET aHEAD* lets try a HEAD request.
This works and gives out the flag:
```flag
flag: picoCTF{r3j3ct_th3_du4l1ty_2e5ba39f}
```

## Solve Script
---
```bash
curl -I http://mercury.picoctf.net:53554/index.php | grep pico | awk -F': ' '{print $2}'
```


---
Creation date: 08-10-2022
Last modified date: Sunday 8th October 2022
***


