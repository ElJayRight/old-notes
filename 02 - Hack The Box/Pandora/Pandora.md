# Enumeration
## Nmap
```bash
nmap -sC -sV 10.10.11.136
```

Webserver on port 80
domain name panda.htb
Nothing on the webserver.

Check UDP with snmpwalk.
Which gives a lot of data. Way to much. :(

Find unique fields.
```bash
grep -oP '::.*?\.' snmpwalk.1 |sort |uniq -c | sort -n
```

hrSWRunParameters. looks interesting
This has creds for daniel
daniel:HotelBabylon23