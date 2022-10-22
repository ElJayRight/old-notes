# Recon
## Nmap
3 ports:
- 22 ssh
- 80 http
- 443 https

## 80
robot.txt
```txt
fsocity.dic
key-1-of-3.txt
```
fsocity.dic is a wordlist.
Dir buster.

found wp-login.php.
This leaks valid usernames.

# Login attempt
## Hydra
with the word list given to enumerate usernames
```bash
hydra -L fsocity.dic -p no 10.10.221.82 http-form-post '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&testcookie=1:F=invalid username'
```
Similar thing for the password.
```bash
hydra -l Elliot -P fsocity.dic 10.10.221.82 http-form-post '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&testcookie=1:S=302'
```

# Reverse Shell
Find a php file on the server and replace it
This gives a shell as the daemon user.
we can move into robot's home dir which has a md5 hash of the password for the user.

# Priv esc
Crack the hash and as ssh is disabled use su to swap to the robot user.
Check for SUID's
nmap is there
nmap is also owned by root so checking gtfobins you can run the sudo priv esc and get root.