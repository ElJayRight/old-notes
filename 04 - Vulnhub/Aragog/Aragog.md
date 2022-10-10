Links [[00 - Global Index (Start Here!)]] [[04 - Vulnhub]]

# [Aragog]
---
## Notes
Nmap scan shows two ports open:
 - 22 ssh
 - 80 http

The landing page on port 80 is an image.
Running feroxbuster shows that it is a wordpress site running from http://192.168.16.6/blog

running wpscan with aggressive plugin search shows 2 plugins.
The not deafult one is wp-file-manager version 6.0, which has an RCE
Checking msfconsole for an easy win.
The exploit works and now we are on the box as www-data.
linpeas.sh shows that there is credentials for the sql database.

logging in a dumping the wp-users table give a hash for hagrid98 cracking with hashcat, and now a ssh session.

Priv esc:

Linpeas.sh showed that there is a file created by hagrid98 called /opt/.backup.sh which is a bash script run by root. Adding a rev shell to the end give root access.

:)



---
Creation date: From old Linux build date unknown
Last modified date: Sunday 9th October 2022
***
