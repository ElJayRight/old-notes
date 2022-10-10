Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Active Directory Basics]]

# [04 - Users + Groups]
## Notes
---
Users Overview
Four main types
- Domain Admins - Can control everything and only one with access to the domain controller
- Service Accounts ( can be Domain Admins) - SQL service account
- Local Administrators - can only make changes to the local machine.
- Domain Users - They can login and exist.

Groups
Two different types
- Security Groups - permissions for a large number of users
- Distribution Groups - email distribution lists (useless)

Default Security Groups
- Domain Controllers - All domain contollers in the domain
- Domain Guests - All domain Guests
- Domain Users - All domain Users
- Domain Computers - All workstations and servers joined to the domain
- Enterprise Admins - Desginated administrators of the enterprise
- Schema Admins - Designated administrators of the schema
- DNS Admins - DNS Administrators Group
- DNS Update Proxy - DNS clients who are permitted to perform dynamic updates on behald of some other clients
- Allowed RODC Password Replication Group - Members in this group can have thier passwords replicated to all read-only domain contollers in the domain
- Group Policy Creator Owners - Members in this group can modify group policy for the domain
- Denied RODC Password Replication Group - Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain.
- Protected Users - Members of this group are afforded additional protectiosn against authentication security threats
- Cert Publishers - Members of this group are permitted to publish certs to the directory
- Read-Only domain controllers - Members of this group are Read-Only Domain Controllers in the domain
- Enterprise Read-Only Domain Controllers - Member of this group are Read-Only Domain Controllers in the enterprise
- Key Admins - Members of this group can perform administrative actions on key objects within the domain.
- Enterprise Key Admins - Members of this group can perform administratice actions on key objects within the forest
- Cloneable Domain Controllers - Members of this gorup that are domain controllers may be cloned.
- RSA and IAS Servers - Servers in this group can access remote access properties of users.