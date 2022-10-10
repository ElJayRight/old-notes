Links [[00 - Global Index (Start Here!)]] [[04 - Vulnhub]]

# [Nagini]
---
## Notes
Running nmap shows 2 ports open:
- 22 ssh
- 80 http
Port 80 dir buster shows a joomla cms

Need to find out how to see the version
msfconsole has one. :)
```bash
use auxiliary/scanner/http/joomla_version
```
version 3.9.25




---
Creation date: From old Linux build date unknown
Last modified date: Sunday 9th October 2022
***
