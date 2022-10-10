Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Attacking Kerberos]]
# [05 - AS-REP Roasting with Rubeus]
## Notes
---
Overview
During pre-auth, the users hash will be used to encrypt a timestamp that the DC will attempt to decrypt to validate that the right has is being used. After validating the timestamp the KDC will then issue a TGT for the user. If pre-auth is disabeld you can request any auth data for any user and the KDC will return an encrypted TGT.

```powershell
Rubeus.exe asreproast
```
```bash
hashcat -m 18200 hash.txt Pass.txt
```