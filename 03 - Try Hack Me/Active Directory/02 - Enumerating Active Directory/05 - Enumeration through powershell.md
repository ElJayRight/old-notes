Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Enumerating Active Directory]]

# [05 - Enumeration through powershell]
## Notes
---
Get-ADUser -Identity <name> -Server <DC> -Properties \*
Get-ADUser -Filter 'Name -like "\*stevens"' -Server <DC> | Format-Table

Get-Group -Identtity Administrators -Server <DC>