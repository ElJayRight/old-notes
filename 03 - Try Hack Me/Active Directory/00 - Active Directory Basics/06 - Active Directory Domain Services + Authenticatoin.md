Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Active Directory Basics]]

# [06 - Active Directory Domain Services + Authenticatoin]
## Notes
---
Domain Services Overview
- LDAP - Lightweight Directory Access Protocol; provides communication between applications and directoy services
- Certificate Services - allows the domain controller to creat, validate, and revoke public key certificates
- DNS, LLMNR, NBT-NS - Domain Name Services for identifying IP hostnames

Domain Authentication Overview
The most vulnerable part of Active Directory
- Kerberos - THe deafult auth service for AD uses ticket-granting tickets and service tickets to authenticate users and give users access to other resources across the domain.
- NTLM - deafult Windows autherntication protocol uses an encrypted challenge/response protocol.
