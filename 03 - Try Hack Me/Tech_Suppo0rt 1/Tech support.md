Links [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]]

# [[Tech support]]
### Contents
***
- [Task Description](Tech%20support#Task%20Description)
- [Notes](Tech%20support#Notes)


### Task Description
---
Find the root flag.

### Notes
---
Nmap scan
4 ports open
22 - ssh
80 - http
139 - smb
445 - smb

Check smb first with smbclient while running a feroxbuster in the background.

On smb there is a file which has a admin password and encrypted sting for subrion. It also leaks the /subrion page 
Putting the encrypted sting into cyberchef gives the password: Scam2021

There is a RCE with a python script in searchsploit which will give a foothold on the box.
upload linpeas.sh

running linpeas.sh shows creds for the database.
With the password ImAScammerLOL!123
login and do a gtfo binary file read to get the root flag.

---
Creation date: 11-10-2022
Last modified date: Tuesday 11th October 2022
***
