Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Breaching Active Directory]]

# [04 - LDAP Bind Credentials]
## Notes
---
Lightweight Directory Access Protocol (LDAP) is similar to NTLM auth. However it diretly verifies the user's creds.

LDAP is included in
- Github
- Jenkins
- Custom-developed web applications
- Printers
- VPNs
The creds are often stored in plain text in configuration files.

LDAP Pass-back Attacks
This can be performed when access is gained to a device;s configuration where LDAP parameters are specified. THis can be a web interface of a network printer. Which have weak creds such as admin:admin or admin:password