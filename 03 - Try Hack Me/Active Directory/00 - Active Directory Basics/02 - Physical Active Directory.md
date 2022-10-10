Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Active Directory Basics]]

# [02 - Physical Active Directory]
## Notes
---
Domian Controllers
- holds the AD DS (Domain Services) data store
- handles autherntication and authorization services
- replicate updates from other domain controllers in the forest
- Allows admin access to manage domain resources
AD DS Data Store
- Contains the NTDS.dit - a database that contains all of the information of an Actie Directory domain controller as well as password hashes for domain users
- Stored by deafult in %SystemRoot%\\NTDS
- accessible only by the domain controller