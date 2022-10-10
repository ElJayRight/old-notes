```bash
# extended LDIF
#
# LDAPv3
# base <dc=active,dc=htb> with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# active.htb
dn: DC=active,DC=htb
objectClass: top
objectClass: domain
objectClass: domainDNS
distinguishedName: DC=active,DC=htb
instanceType: 5
whenCreated: 20180718184900.0Z
whenChanged: 20220429152618.0Z
subRefs: DC=ForestDnsZones,DC=active,DC=htb
subRefs: DC=DomainDnsZones,DC=active,DC=htb
subRefs: CN=Configuration,DC=active,DC=htb
uSNCreated: 4099
uSNChanged: 94232
name: active
objectGUID:: XIZQu8xN1k62JVkdAGr3Jg==
creationTime: 132957195784512192
forceLogoff: -9223372036854775808
lockoutDuration: -18000000000
lockOutObservationWindow: -18000000000
lockoutThreshold: 0
maxPwdAge: -36288000000000
minPwdAge: -864000000000
minPwdLength: 7
modifiedCountAtLastProm: 0
nextRid: 1000
pwdProperties: 1
pwdHistoryLength: 24
objectSid:: AQQAAAAAAAUVAAAArxktGAS1AL49Gv12
serverState: 1
uASCompat: 1
modifiedCount: 1
auditingPolicy:: AAE=
nTMixedDomain: 0
rIDManagerReference: CN=RID Manager$,CN=System,DC=active,DC=htb
fSMORoleOwner: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN
 =Sites,CN=Configuration,DC=active,DC=htb
systemFlags: -1946157056
wellKnownObjects: B:32:6227F0AF1FC2410D8E3BB10615BB5B0F:CN=NTDS Quotas,DC=acti
 ve,DC=htb
wellKnownObjects: B:32:F4BE92A4C777485E878E9421D53087DB:CN=Microsoft,CN=Progra
 m Data,DC=active,DC=htb
wellKnownObjects: B:32:09460C08AE1E4A4EA0F64AEE7DAA1E5A:CN=Program Data,DC=act
 ive,DC=htb
wellKnownObjects: B:32:22B70C67D56E4EFB91E9300FCA3DC1AA:CN=ForeignSecurityPrin
 cipals,DC=active,DC=htb
wellKnownObjects: B:32:18E2EA80684F11D2B9AA00C04F79F805:CN=Deleted Objects,DC=
 active,DC=htb
wellKnownObjects: B:32:2FBAC1870ADE11D297C400C04FD8D5CD:CN=Infrastructure,DC=a
 ctive,DC=htb
wellKnownObjects: B:32:AB8153B7768811D1ADED00C04FD8D5CD:CN=LostAndFound,DC=act
 ive,DC=htb
wellKnownObjects: B:32:AB1D30F3768811D1ADED00C04FD8D5CD:CN=System,DC=active,DC
 =htb
wellKnownObjects: B:32:A361B2FFFFD211D1AA4B00C04FD7D83A:OU=Domain Controllers,
 DC=active,DC=htb
wellKnownObjects: B:32:AA312825768811D1ADED00C04FD8D5CD:CN=Computers,DC=active
 ,DC=htb
wellKnownObjects: B:32:A9D1CA15768811D1ADED00C04FD8D5CD:CN=Users,DC=active,DC=
 htb
objectCategory: CN=Domain-DNS,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
gPLink: [LDAP://CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=Syste
 m,DC=active,DC=htb;0]
dSCorePropagationData: 16010101000000.0Z
otherWellKnownObjects: B:32:1EB93889E40C45DF9F0C64D23BBB6237:CN=Managed Servic
 e Accounts,DC=active,DC=htb
masteredBy: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Si
 tes,CN=Configuration,DC=active,DC=htb
ms-DS-MachineAccountQuota: 10
msDS-Behavior-Version: 4
msDS-PerUserTrustQuota: 1
msDS-AllUsersTrustQuota: 1000
msDS-PerUserTrustTombstonesQuota: 10
msDs-masteredBy: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,
 CN=Sites,CN=Configuration,DC=active,DC=htb
msDS-IsDomainFor: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name
 ,CN=Sites,CN=Configuration,DC=active,DC=htb
msDS-NcType: 0
dc: active

# Users, active.htb
dn: CN=Users,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Users
description: Default container for upgraded user accounts
distinguishedName: CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5696
uSNChanged: 5696
showInAdvancedViewOnly: FALSE
name: Users
objectGUID:: lu1lON+Sdke7Y8hkC5Zk1g==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Computers, active.htb
dn: CN=Computers,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Computers
description: Default container for upgraded computer accounts
distinguishedName: CN=Computers,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5697
uSNChanged: 5697
showInAdvancedViewOnly: FALSE
name: Computers
objectGUID:: jahtqHd15U+nE84PrtANWg==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Domain Controllers, active.htb
dn: OU=Domain Controllers,DC=active,DC=htb
objectClass: top
objectClass: organizationalUnit
ou: Domain Controllers
description: Default container for domain controllers
distinguishedName: OU=Domain Controllers,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5828
uSNChanged: 5828
showInAdvancedViewOnly: FALSE
name: Domain Controllers
objectGUID:: 4noWM9ZmVECfLQFICct5sg==
systemFlags: -1946157056
objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=active,DC
 =htb
isCriticalSystemObject: TRUE
gPLink: [LDAP://CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=Syste
 m,DC=active,DC=htb;0]
dSCorePropagationData: 16010101000000.0Z

# System, active.htb
dn: CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: System
description: Builtin system settings
distinguishedName: CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5698
uSNChanged: 5698
showInAdvancedViewOnly: TRUE
name: System
objectGUID:: 9U49dy9mzEKoahPhmB9i1Q==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# LostAndFound, active.htb
dn: CN=LostAndFound,DC=active,DC=htb
objectClass: top
objectClass: lostAndFound
cn: LostAndFound
description: Default container for orphaned objects
distinguishedName: CN=LostAndFound,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5694
uSNChanged: 5694
showInAdvancedViewOnly: TRUE
name: LostAndFound
objectGUID:: 1KpGO98nlEmVTkogLK0WgA==
systemFlags: -1946157056
objectCategory: CN=Lost-And-Found,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Infrastructure, active.htb
dn: CN=Infrastructure,DC=active,DC=htb
objectClass: top
objectClass: infrastructureUpdate
cn: Infrastructure
distinguishedName: CN=Infrastructure,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5829
uSNChanged: 5829
showInAdvancedViewOnly: TRUE
name: Infrastructure
objectGUID:: OYUOJU6oPEODqyXzWfVmQA==
fSMORoleOwner: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN
 =Sites,CN=Configuration,DC=active,DC=htb
systemFlags: -1946157056
objectCategory: CN=Infrastructure-Update,CN=Schema,CN=Configuration,DC=active,
 DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# ForeignSecurityPrincipals, active.htb
dn: CN=ForeignSecurityPrincipals,DC=active,DC=htb
objectClass: top
objectClass: container
cn: ForeignSecurityPrincipals
description: Default container for security identifiers (SIDs) associated with
  objects from external, trusted domains
distinguishedName: CN=ForeignSecurityPrincipals,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5830
uSNChanged: 5830
showInAdvancedViewOnly: FALSE
name: ForeignSecurityPrincipals
objectGUID:: S48iHIH2K0Kdxnw/SSn6ww==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Program Data, active.htb
dn: CN=Program Data,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Program Data
description: Default location for storage of application data.
distinguishedName: CN=Program Data,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5831
uSNChanged: 5831
showInAdvancedViewOnly: TRUE
name: Program Data
objectGUID:: uhVHeKoFyEqvVeLjHgwibw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# Microsoft, Program Data, active.htb
dn: CN=Microsoft,CN=Program Data,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Microsoft
description: Default location for storage of Microsoft application data.
distinguishedName: CN=Microsoft,CN=Program Data,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5832
uSNChanged: 5832
showInAdvancedViewOnly: TRUE
name: Microsoft
objectGUID:: 9uMcUq0EeUmfOlO64vhbHg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# NTDS Quotas, active.htb
dn: CN=NTDS Quotas,DC=active,DC=htb

# Managed Service Accounts, active.htb
dn: CN=Managed Service Accounts,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Managed Service Accounts
description: Default container for managed service accounts
distinguishedName: CN=Managed Service Accounts,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5834
uSNChanged: 5834
showInAdvancedViewOnly: FALSE
name: Managed Service Accounts
objectGUID:: RCMEhFJ8a0+4QAXa4K1+dA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# WinsockServices, System, active.htb
dn: CN=WinsockServices,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: WinsockServices
distinguishedName: CN=WinsockServices,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5699
uSNChanged: 5699
showInAdvancedViewOnly: TRUE
name: WinsockServices
objectGUID:: ZGp89HKzqEaf4cNYGkK2Sw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# RpcServices, System, active.htb
dn: CN=RpcServices,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
objectClass: rpcContainer
cn: RpcServices
distinguishedName: CN=RpcServices,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5700
uSNChanged: 5700
showInAdvancedViewOnly: TRUE
name: RpcServices
objectGUID:: zML5RCLB50OSNKYRGeLcaQ==
systemFlags: -1946157056
objectCategory: CN=Rpc-Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# FileLinks, System, active.htb
dn: CN=FileLinks,CN=System,DC=active,DC=htb
objectClass: top
objectClass: fileLinkTracking
cn: FileLinks
distinguishedName: CN=FileLinks,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5701
uSNChanged: 5701
showInAdvancedViewOnly: TRUE
name: FileLinks
objectGUID:: L4ydJr+XSUitKHJQsHbqDw==
systemFlags: -1946157056
objectCategory: CN=File-Link-Tracking,CN=Schema,CN=Configuration,DC=active,DC=
 htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# VolumeTable, FileLinks, System, active.htb
dn: CN=VolumeTable,CN=FileLinks,CN=System,DC=active,DC=htb

# ObjectMoveTable, FileLinks, System, active.htb
dn: CN=ObjectMoveTable,CN=FileLinks,CN=System,DC=active,DC=htb
objectClass: top
objectClass: fileLinkTracking
objectClass: linkTrackObjectMoveTable
cn: ObjectMoveTable
distinguishedName: CN=ObjectMoveTable,CN=FileLinks,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5703
uSNChanged: 5703
showInAdvancedViewOnly: TRUE
name: ObjectMoveTable
objectGUID:: HY6vcyDYkE26x/CaiIZz9g==
systemFlags: -1946157056
objectCategory: CN=Link-Track-Object-Move-Table,CN=Schema,CN=Configuration,DC=
 active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Default Domain Policy, System, active.htb
dn: CN=Default Domain Policy,CN=System,DC=active,DC=htb
objectClass: top
objectClass: leaf
objectClass: domainPolicy
cn: Default Domain Policy
distinguishedName: CN=Default Domain Policy,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5704
uSNChanged: 5704
showInAdvancedViewOnly: TRUE
name: Default Domain Policy
objectGUID:: OG53/meX6U6uIzHRDgemvw==
objectCategory: CN=Domain-Policy,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# AppCategories, Default Domain Policy, System, active.htb
dn: CN=AppCategories,CN=Default Domain Policy,CN=System,DC=active,DC=htb
objectClass: top
objectClass: classStore
cn: AppCategories
distinguishedName: CN=AppCategories,CN=Default Domain Policy,CN=System,DC=acti
 ve,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5705
uSNChanged: 5705
showInAdvancedViewOnly: TRUE
name: AppCategories
objectGUID:: 4V1gSNLxFUqBzsewAa6yjg==
objectCategory: CN=Class-Store,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Meetings, System, active.htb
dn: CN=Meetings,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Meetings
distinguishedName: CN=Meetings,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5706
uSNChanged: 5706
showInAdvancedViewOnly: TRUE
name: Meetings
objectGUID:: tYs3WHNKcEWAnaJxZeLMRg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Policies, System, active.htb
dn: CN=Policies,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Policies
distinguishedName: CN=Policies,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5707
uSNChanged: 5707
showInAdvancedViewOnly: TRUE
name: Policies
objectGUID:: N6/qMx404E2zKReqoyCc2A==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# {31B2F340-016D-11D2-945F-00C04FB984F9}, Policies, System, active.htb
dn: CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=active,
 DC=htb
objectClass: top
objectClass: container
objectClass: groupPolicyContainer
cn: {31B2F340-016D-11D2-945F-00C04FB984F9}
distinguishedName: CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=Sy
 stem,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718204606.0Z
displayName: Default Domain Policy
uSNCreated: 5708
uSNChanged: 24616
showInAdvancedViewOnly: TRUE
name: {31B2F340-016D-11D2-945F-00C04FB984F9}
objectGUID:: YynkYMjy/ECKsMAXbX+16Q==
flags: 0
versionNumber: 11
systemFlags: -1946157056
objectCategory: CN=Group-Policy-Container,CN=Schema,CN=Configuration,DC=active
 ,DC=htb
isCriticalSystemObject: TRUE
gPCFunctionalityVersion: 2
gPCFileSysPath: \\active.htb\sysvol\active.htb\Policies\{31B2F340-016D-11D2-94
 5F-00C04FB984F9}
gPCMachineExtensionNames: [{00000000-0000-0000-0000-000000000000}{79F92669-422
 4-476C-9C5C-6EFB4D87DF4A}][{17D89FEC-5C44-4972-B12D-241CAEF74509}{79F92669-42
 24-476C-9C5C-6EFB4D87DF4A}][{35378EAC-683F-11D2-A89A-00C04FBBCFA2}{53D6AB1B-2
 488-11D1-A28C-00C04FB94F17}][{827D319E-6EAC-11D2-A4EA-00C04F79F83A}{803E14A0-
 B4FB-11D0-A0D0-00A0C90F574B}][{B1BE8D72-6EAC-11D2-A4EA-00C04F79F83A}{53D6AB1B
 -2488-11D1-A28C-00C04FB94F17}]
dSCorePropagationData: 16010101000000.0Z

# User, {31B2F340-016D-11D2-945F-00C04FB984F9}, Policies, System, active.htb
dn: CN=User,CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC
 =active,DC=htb
objectClass: top
objectClass: container
cn: User
distinguishedName: CN=User,CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Polici
 es,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5709
uSNChanged: 5709
showInAdvancedViewOnly: TRUE
name: User
objectGUID:: FD1OPoh0YkyMpLD3H5fNyw==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Machine, {31B2F340-016D-11D2-945F-00C04FB984F9}, Policies, System, active.htb
dn: CN=Machine,CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System
 ,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Machine
distinguishedName: CN=Machine,CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Pol
 icies,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5710
uSNChanged: 5710
showInAdvancedViewOnly: TRUE
name: Machine
objectGUID:: TsX8YDP2/kigDHel6vZNbw==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# {6AC1786C-016F-11D2-945F-00C04fB984F9}, Policies, System, active.htb
dn: CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC=active,
 DC=htb
objectClass: top
objectClass: container
objectClass: groupPolicyContainer
cn: {6AC1786C-016F-11D2-945F-00C04fB984F9}
distinguishedName: CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=Sy
 stem,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180721133545.0Z
displayName: Default Domain Controllers Policy
uSNCreated: 5711
uSNChanged: 36887
showInAdvancedViewOnly: TRUE
name: {6AC1786C-016F-11D2-945F-00C04fB984F9}
objectGUID:: MBY228RhIUq4/qGAskqecQ==
flags: 0
versionNumber: 29
systemFlags: -1946157056
objectCategory: CN=Group-Policy-Container,CN=Schema,CN=Configuration,DC=active
 ,DC=htb
isCriticalSystemObject: TRUE
gPCFunctionalityVersion: 2
gPCFileSysPath: \\active.htb\sysvol\active.htb\Policies\{6AC1786C-016F-11D2-94
 5F-00C04fB984F9}
gPCMachineExtensionNames: [{827D319E-6EAC-11D2-A4EA-00C04F79F83A}{803E14A0-B4F
 B-11D0-A0D0-00A0C90F574B}]
dSCorePropagationData: 16010101000000.0Z

# User, {6AC1786C-016F-11D2-945F-00C04fB984F9}, Policies, System, active.htb
dn: CN=User,CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC
 =active,DC=htb
objectClass: top
objectClass: container
cn: User
distinguishedName: CN=User,CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Polici
 es,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5712
uSNChanged: 5712
showInAdvancedViewOnly: TRUE
name: User
objectGUID:: 4QKP60QVhkuB6Pf3MkwLbA==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Machine, {6AC1786C-016F-11D2-945F-00C04fB984F9}, Policies, System, active.htb
dn: CN=Machine,CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System
 ,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Machine
distinguishedName: CN=Machine,CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Pol
 icies,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5713
uSNChanged: 5713
showInAdvancedViewOnly: TRUE
name: Machine
objectGUID:: 4xlVUCpDG066PQGIltS31w==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# RAS and IAS Servers Access Check, System, active.htb
dn: CN=RAS and IAS Servers Access Check,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: RAS and IAS Servers Access Check
distinguishedName: CN=RAS and IAS Servers Access Check,CN=System,DC=active,DC=
 htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5714
uSNChanged: 5714
showInAdvancedViewOnly: TRUE
name: RAS and IAS Servers Access Check
objectGUID:: EuboSKehAEelwv3U+GudGQ==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# File Replication Service, System, active.htb
dn: CN=File Replication Service,CN=System,DC=active,DC=htb
objectClass: top
objectClass: applicationSettings
objectClass: nTFRSSettings
cn: File Replication Service
distinguishedName: CN=File Replication Service,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5715
uSNChanged: 5715
showInAdvancedViewOnly: TRUE
name: File Replication Service
objectGUID:: WKxmbdFHJ0yBUKfD1IBcvw==
systemFlags: -1946157056
objectCategory: CN=NTFRS-Settings,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Dfs-Configuration, System, active.htb
dn: CN=Dfs-Configuration,CN=System,DC=active,DC=htb
objectClass: top
objectClass: dfsConfiguration
cn: Dfs-Configuration
distinguishedName: CN=Dfs-Configuration,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5716
uSNChanged: 5716
showInAdvancedViewOnly: FALSE
name: Dfs-Configuration
objectGUID:: c7Pmyr+xKkm3YEluRi0nGw==
objectCategory: CN=Dfs-Configuration,CN=Schema,CN=Configuration,DC=active,DC=h
 tb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# IP Security, System, active.htb
dn: CN=IP Security,CN=System,DC=active,DC=htb

# ipsecPolicy{72385230-70FA-11D1-864C-14A300000000}, IP Security, System, activ
 e.htb
dn: CN=ipsecPolicy{72385230-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys
 tem,DC=active,DC=htb

# ipsecISAKMPPolicy{72385231-70FA-11D1-864C-14A300000000}, IP Security, System,
  active.htb
dn: CN=ipsecISAKMPPolicy{72385231-70FA-11D1-864C-14A300000000},CN=IP Security,
 CN=System,DC=active,DC=htb

# ipsecNFA{72385232-70FA-11D1-864C-14A300000000}, IP Security, System, active.h
 tb
dn: CN=ipsecNFA{72385232-70FA-11D1-864C-14A300000000},CN=IP Security,CN=System
 ,DC=active,DC=htb

# ipsecNFA{59319BE2-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, System, active.h
 tb
dn: CN=ipsecNFA{59319BE2-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Security,CN=System
 ,DC=active,DC=htb

# ipsecNFA{594272E2-071D-11D3-AD22-0060B0ECCA17}, IP Security, System, active.h
 tb
dn: CN=ipsecNFA{594272E2-071D-11D3-AD22-0060B0ECCA17},CN=IP Security,CN=System
 ,DC=active,DC=htb

# ipsecNegotiationPolicy{72385233-70FA-11D1-864C-14A300000000}, IP Security, Sy
 stem, active.htb
dn: CN=ipsecNegotiationPolicy{72385233-70FA-11D1-864C-14A300000000},CN=IP Secu
 rity,CN=System,DC=active,DC=htb

# ipsecFilter{7238523A-70FA-11D1-864C-14A300000000}, IP Security, System, activ
 e.htb
dn: CN=ipsecFilter{7238523A-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys
 tem,DC=active,DC=htb

# ipsecNegotiationPolicy{59319BDF-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, Sy
 stem, active.htb
dn: CN=ipsecNegotiationPolicy{59319BDF-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Secu
 rity,CN=System,DC=active,DC=htb

# ipsecNegotiationPolicy{7238523B-70FA-11D1-864C-14A300000000}, IP Security, Sy
 stem, active.htb
dn: CN=ipsecNegotiationPolicy{7238523B-70FA-11D1-864C-14A300000000},CN=IP Secu
 rity,CN=System,DC=active,DC=htb

# ipsecFilter{72385235-70FA-11D1-864C-14A300000000}, IP Security, System, activ
 e.htb
dn: CN=ipsecFilter{72385235-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys
 tem,DC=active,DC=htb

# ipsecPolicy{72385236-70FA-11D1-864C-14A300000000}, IP Security, System, activ
 e.htb
dn: CN=ipsecPolicy{72385236-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys
 tem,DC=active,DC=htb

# ipsecISAKMPPolicy{72385237-70FA-11D1-864C-14A300000000}, IP Security, System,
  active.htb
dn: CN=ipsecISAKMPPolicy{72385237-70FA-11D1-864C-14A300000000},CN=IP Security,
 CN=System,DC=active,DC=htb

# ipsecNFA{59319C04-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, System, active.h
 tb
dn: CN=ipsecNFA{59319C04-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Security,CN=System
 ,DC=active,DC=htb

# ipsecNegotiationPolicy{59319C01-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, Sy
 stem, active.htb
dn: CN=ipsecNegotiationPolicy{59319C01-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Secu
 rity,CN=System,DC=active,DC=htb

# ipsecPolicy{7238523C-70FA-11D1-864C-14A300000000}, IP Security, System, activ
 e.htb
dn: CN=ipsecPolicy{7238523C-70FA-11D1-864C-14A300000000},CN=IP Security,CN=Sys
 tem,DC=active,DC=htb

# ipsecISAKMPPolicy{7238523D-70FA-11D1-864C-14A300000000}, IP Security, System,
  active.htb
dn: CN=ipsecISAKMPPolicy{7238523D-70FA-11D1-864C-14A300000000},CN=IP Security,
 CN=System,DC=active,DC=htb

# ipsecNFA{7238523E-70FA-11D1-864C-14A300000000}, IP Security, System, active.h
 tb
dn: CN=ipsecNFA{7238523E-70FA-11D1-864C-14A300000000},CN=IP Security,CN=System
 ,DC=active,DC=htb

# ipsecNFA{59319BF3-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, System, active.h
 tb
dn: CN=ipsecNFA{59319BF3-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Security,CN=System
 ,DC=active,DC=htb

# ipsecNFA{594272FD-071D-11D3-AD22-0060B0ECCA17}, IP Security, System, active.h
 tb
dn: CN=ipsecNFA{594272FD-071D-11D3-AD22-0060B0ECCA17},CN=IP Security,CN=System
 ,DC=active,DC=htb

# ipsecNegotiationPolicy{7238523F-70FA-11D1-864C-14A300000000}, IP Security, Sy
 stem, active.htb
dn: CN=ipsecNegotiationPolicy{7238523F-70FA-11D1-864C-14A300000000},CN=IP Secu
 rity,CN=System,DC=active,DC=htb

# ipsecNegotiationPolicy{59319BF0-5EE3-11D2-ACE8-0060B0ECCA17}, IP Security, Sy
 stem, active.htb
dn: CN=ipsecNegotiationPolicy{59319BF0-5EE3-11D2-ACE8-0060B0ECCA17},CN=IP Secu
 rity,CN=System,DC=active,DC=htb

# ipsecNFA{6A1F5C6F-72B7-11D2-ACF0-0060B0ECCA17}, IP Security, System, active.h
 tb
dn: CN=ipsecNFA{6A1F5C6F-72B7-11D2-ACF0-0060B0ECCA17},CN=IP Security,CN=System
 ,DC=active,DC=htb

# AdminSDHolder, System, active.htb
dn: CN=AdminSDHolder,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: AdminSDHolder
distinguishedName: CN=AdminSDHolder,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 5740
uSNChanged: 12722
showInAdvancedViewOnly: TRUE
name: AdminSDHolder
objectGUID:: 4LQyTAAFP0qG5x9P1rvIOQ==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20220429154128.0Z
dSCorePropagationData: 20210121162036.0Z
dSCorePropagationData: 20180730145206.0Z
dSCorePropagationData: 20180730140358.0Z
dSCorePropagationData: 16010101000000.0Z

# ComPartitions, System, active.htb
dn: CN=ComPartitions,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: ComPartitions
distinguishedName: CN=ComPartitions,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5741
uSNChanged: 5741
showInAdvancedViewOnly: TRUE
name: ComPartitions
objectGUID:: NvgRsnV1sEas5qNuiaQElg==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# ComPartitionSets, System, active.htb
dn: CN=ComPartitionSets,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: ComPartitionSets
distinguishedName: CN=ComPartitionSets,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5742
uSNChanged: 5742
showInAdvancedViewOnly: TRUE
name: ComPartitionSets
objectGUID:: mFetGo0t9UKApSwvfP23Rg==
systemFlags: -1946157056
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# WMIPolicy, System, active.htb
dn: CN=WMIPolicy,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: WMIPolicy
distinguishedName: CN=WMIPolicy,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5743
uSNChanged: 5743
showInAdvancedViewOnly: TRUE
name: WMIPolicy
objectGUID:: 0qPV1eojFEaLz6MiJBxoyQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# PolicyTemplate, WMIPolicy, System, active.htb
dn: CN=PolicyTemplate,CN=WMIPolicy,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: PolicyTemplate
distinguishedName: CN=PolicyTemplate,CN=WMIPolicy,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5744
uSNChanged: 5744
showInAdvancedViewOnly: TRUE
name: PolicyTemplate
objectGUID:: cFGu9IJA90KA5wNXW6wAsw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# SOM, WMIPolicy, System, active.htb
dn: CN=SOM,CN=WMIPolicy,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: SOM
distinguishedName: CN=SOM,CN=WMIPolicy,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5745
uSNChanged: 5745
showInAdvancedViewOnly: TRUE
name: SOM
objectGUID:: yRFivAFj1kWgxmjhSn/jog==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# PolicyType, WMIPolicy, System, active.htb
dn: CN=PolicyType,CN=WMIPolicy,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: PolicyType
distinguishedName: CN=PolicyType,CN=WMIPolicy,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5746
uSNChanged: 5746
showInAdvancedViewOnly: TRUE
name: PolicyType
objectGUID:: DQmG2pmdMkiUgbs+0+Cbvg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# WMIGPO, WMIPolicy, System, active.htb
dn: CN=WMIGPO,CN=WMIPolicy,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: WMIGPO
distinguishedName: CN=WMIGPO,CN=WMIPolicy,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5747
uSNChanged: 5747
showInAdvancedViewOnly: TRUE
name: WMIGPO
objectGUID:: rvBPZWbw4km7I0EnQAdaKw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# DomainUpdates, System, active.htb
dn: CN=DomainUpdates,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: DomainUpdates
distinguishedName: CN=DomainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5748
uSNChanged: 5748
showInAdvancedViewOnly: TRUE
name: DomainUpdates
objectGUID:: U4K9/Xhd1kulhq8wAaRwYA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# Operations, DomainUpdates, System, active.htb
dn: CN=Operations,CN=DomainUpdates,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Operations
distinguishedName: CN=Operations,CN=DomainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5749
uSNChanged: 5749
showInAdvancedViewOnly: TRUE
name: Operations
objectGUID:: y1Ys061o00GOEIzcJ0MkOA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# ab402345-d3c3-455d-9ff7-40268a1099b6, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=ab402345-d3c3-455d-9ff7-40268a1099b6,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: ab402345-d3c3-455d-9ff7-40268a1099b6
distinguishedName: CN=ab402345-d3c3-455d-9ff7-40268a1099b6,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5750
uSNChanged: 5750
showInAdvancedViewOnly: TRUE
name: ab402345-d3c3-455d-9ff7-40268a1099b6
objectGUID:: wiDNp9wAk0KpOFjUu9cghw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# bab5f54d-06c8-48de-9b87-d78b796564e4, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=bab5f54d-06c8-48de-9b87-d78b796564e4,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: bab5f54d-06c8-48de-9b87-d78b796564e4
distinguishedName: CN=bab5f54d-06c8-48de-9b87-d78b796564e4,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5751
uSNChanged: 5751
showInAdvancedViewOnly: TRUE
name: bab5f54d-06c8-48de-9b87-d78b796564e4
objectGUID:: Uyng3h0TYUWIGU6deQhhNw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5
distinguishedName: CN=f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5752
uSNChanged: 5752
showInAdvancedViewOnly: TRUE
name: f3dd09dd-25e8-4f9c-85df-12d6d2f2f2f5
objectGUID:: Ryv2ccAFKEK3LKO23hfwSw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 2416c60a-fe15-4d7a-a61e-dffd5df864d3, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=2416c60a-fe15-4d7a-a61e-dffd5df864d3,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 2416c60a-fe15-4d7a-a61e-dffd5df864d3
distinguishedName: CN=2416c60a-fe15-4d7a-a61e-dffd5df864d3,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5753
uSNChanged: 5753
showInAdvancedViewOnly: TRUE
name: 2416c60a-fe15-4d7a-a61e-dffd5df864d3
objectGUID:: JVgx0aLj0EyVz5w6tWjyKQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 7868d4c8-ac41-4e05-b401-776280e8e9f1, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=7868d4c8-ac41-4e05-b401-776280e8e9f1,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 7868d4c8-ac41-4e05-b401-776280e8e9f1
distinguishedName: CN=7868d4c8-ac41-4e05-b401-776280e8e9f1,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5754
uSNChanged: 5754
showInAdvancedViewOnly: TRUE
name: 7868d4c8-ac41-4e05-b401-776280e8e9f1
objectGUID:: M9jtjyVRlE28NRwt3lRuvQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 860c36ed-5241-4c62-a18b-cf6ff9994173, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=860c36ed-5241-4c62-a18b-cf6ff9994173,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 860c36ed-5241-4c62-a18b-cf6ff9994173
distinguishedName: CN=860c36ed-5241-4c62-a18b-cf6ff9994173,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5755
uSNChanged: 5755
showInAdvancedViewOnly: TRUE
name: 860c36ed-5241-4c62-a18b-cf6ff9994173
objectGUID:: P3CTz6xKPE27T06EJR3dog==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e
distinguishedName: CN=0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5756
uSNChanged: 5756
showInAdvancedViewOnly: TRUE
name: 0e660ea3-8a5e-4495-9ad7-ca1bd4638f9e
objectGUID:: 9pK7kUX6G0aKEDTXkjDeLw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# a86fe12a-0f62-4e2a-b271-d27f601f8182, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=a86fe12a-0f62-4e2a-b271-d27f601f8182,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: a86fe12a-0f62-4e2a-b271-d27f601f8182
distinguishedName: CN=a86fe12a-0f62-4e2a-b271-d27f601f8182,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5757
uSNChanged: 5757
showInAdvancedViewOnly: TRUE
name: a86fe12a-0f62-4e2a-b271-d27f601f8182
objectGUID:: hIhoFcaGx0ObABusmcL7NQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# d85c0bfd-094f-4cad-a2b5-82ac9268475d, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=d85c0bfd-094f-4cad-a2b5-82ac9268475d,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: d85c0bfd-094f-4cad-a2b5-82ac9268475d
distinguishedName: CN=d85c0bfd-094f-4cad-a2b5-82ac9268475d,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5758
uSNChanged: 5758
showInAdvancedViewOnly: TRUE
name: d85c0bfd-094f-4cad-a2b5-82ac9268475d
objectGUID:: OWrq9+nJrUu5+rQE71aIHA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6ada9ff7-c9df-45c1-908e-9fef2fab008a, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6ada9ff7-c9df-45c1-908e-9fef2fab008a,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6ada9ff7-c9df-45c1-908e-9fef2fab008a
distinguishedName: CN=6ada9ff7-c9df-45c1-908e-9fef2fab008a,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5759
uSNChanged: 5759
showInAdvancedViewOnly: TRUE
name: 6ada9ff7-c9df-45c1-908e-9fef2fab008a
objectGUID:: X0W2w6Qhe0G6bd9nC81iiA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 10b3ad2a-6883-4fa7-90fc-6377cbdc1b26, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=10b3ad2a-6883-4fa7-90fc-6377cbdc1b26,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 10b3ad2a-6883-4fa7-90fc-6377cbdc1b26
distinguishedName: CN=10b3ad2a-6883-4fa7-90fc-6377cbdc1b26,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5760
uSNChanged: 5760
showInAdvancedViewOnly: TRUE
name: 10b3ad2a-6883-4fa7-90fc-6377cbdc1b26
objectGUID:: RSUbl5sh3EuAcSw0p7dxeQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 98de1d3e-6611-443b-8b4e-f4337f1ded0b, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=98de1d3e-6611-443b-8b4e-f4337f1ded0b,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 98de1d3e-6611-443b-8b4e-f4337f1ded0b
distinguishedName: CN=98de1d3e-6611-443b-8b4e-f4337f1ded0b,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5761
uSNChanged: 5761
showInAdvancedViewOnly: TRUE
name: 98de1d3e-6611-443b-8b4e-f4337f1ded0b
objectGUID:: oc8s/wAtNEujIKMnPeITuQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# f607fd87-80cf-45e2-890b-6cf97ec0e284, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=f607fd87-80cf-45e2-890b-6cf97ec0e284,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: f607fd87-80cf-45e2-890b-6cf97ec0e284
distinguishedName: CN=f607fd87-80cf-45e2-890b-6cf97ec0e284,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5762
uSNChanged: 5762
showInAdvancedViewOnly: TRUE
name: f607fd87-80cf-45e2-890b-6cf97ec0e284
objectGUID:: AMZUQvyFpk2QvhBI73IbXQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 9cac1f66-2167-47ad-a472-2a13251310e4, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=9cac1f66-2167-47ad-a472-2a13251310e4,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 9cac1f66-2167-47ad-a472-2a13251310e4
distinguishedName: CN=9cac1f66-2167-47ad-a472-2a13251310e4,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5763
uSNChanged: 5763
showInAdvancedViewOnly: TRUE
name: 9cac1f66-2167-47ad-a472-2a13251310e4
objectGUID:: AM0p+R3xFkyuXO4130w4IA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6ff880d6-11e7-4ed1-a20f-aac45da48650, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6ff880d6-11e7-4ed1-a20f-aac45da48650,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6ff880d6-11e7-4ed1-a20f-aac45da48650
distinguishedName: CN=6ff880d6-11e7-4ed1-a20f-aac45da48650,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5764
uSNChanged: 5764
showInAdvancedViewOnly: TRUE
name: 6ff880d6-11e7-4ed1-a20f-aac45da48650
objectGUID:: O3l5FbU+d0CHa+iLG5F60A==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 446f24ea-cfd5-4c52-8346-96e170bcb912, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=446f24ea-cfd5-4c52-8346-96e170bcb912,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 446f24ea-cfd5-4c52-8346-96e170bcb912
distinguishedName: CN=446f24ea-cfd5-4c52-8346-96e170bcb912,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5765
uSNChanged: 5765
showInAdvancedViewOnly: TRUE
name: 446f24ea-cfd5-4c52-8346-96e170bcb912
objectGUID:: 3agcm2WGwUy+z9K/5i+ybA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 51cba88b-99cf-4e16-bef2-c427b38d0767, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=51cba88b-99cf-4e16-bef2-c427b38d0767,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 51cba88b-99cf-4e16-bef2-c427b38d0767
distinguishedName: CN=51cba88b-99cf-4e16-bef2-c427b38d0767,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5766
uSNChanged: 5766
showInAdvancedViewOnly: TRUE
name: 51cba88b-99cf-4e16-bef2-c427b38d0767
objectGUID:: 7qCKOvVDO0iLXqv2ZMqieg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# a3dac986-80e7-4e59-a059-54cb1ab43cb9, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=a3dac986-80e7-4e59-a059-54cb1ab43cb9,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: a3dac986-80e7-4e59-a059-54cb1ab43cb9
distinguishedName: CN=a3dac986-80e7-4e59-a059-54cb1ab43cb9,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5767
uSNChanged: 5767
showInAdvancedViewOnly: TRUE
name: a3dac986-80e7-4e59-a059-54cb1ab43cb9
objectGUID:: qS3mF6w7MUKddWYQh7hWlg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 293f0798-ea5c-4455-9f5d-45f33a30703b, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=293f0798-ea5c-4455-9f5d-45f33a30703b,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 293f0798-ea5c-4455-9f5d-45f33a30703b
distinguishedName: CN=293f0798-ea5c-4455-9f5d-45f33a30703b,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5768
uSNChanged: 5768
showInAdvancedViewOnly: TRUE
name: 293f0798-ea5c-4455-9f5d-45f33a30703b
objectGUID:: JWp1iT9wBEWDKrPTftiMlg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 5c82b233-75fc-41b3-ac71-c69592e6bf15, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=5c82b233-75fc-41b3-ac71-c69592e6bf15,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 5c82b233-75fc-41b3-ac71-c69592e6bf15
distinguishedName: CN=5c82b233-75fc-41b3-ac71-c69592e6bf15,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5769
uSNChanged: 5769
showInAdvancedViewOnly: TRUE
name: 5c82b233-75fc-41b3-ac71-c69592e6bf15
objectGUID:: KwoQC4AUDkq7GFX5oiq1Ww==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 7ffef925-405b-440a-8d58-35e8cd6e98c3, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=7ffef925-405b-440a-8d58-35e8cd6e98c3,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 7ffef925-405b-440a-8d58-35e8cd6e98c3
distinguishedName: CN=7ffef925-405b-440a-8d58-35e8cd6e98c3,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5770
uSNChanged: 5770
showInAdvancedViewOnly: TRUE
name: 7ffef925-405b-440a-8d58-35e8cd6e98c3
objectGUID:: CoYZmZCl7Eq2PVo5AGpbQQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 4dfbb973-8a62-4310-a90c-776e00f83222, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=4dfbb973-8a62-4310-a90c-776e00f83222,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 4dfbb973-8a62-4310-a90c-776e00f83222
distinguishedName: CN=4dfbb973-8a62-4310-a90c-776e00f83222,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5771
uSNChanged: 5771
showInAdvancedViewOnly: TRUE
name: 4dfbb973-8a62-4310-a90c-776e00f83222
objectGUID:: oj5Sislxx0W7I+mtp4swAg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 8437C3D8-7689-4200-BF38-79E4AC33DFA0, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=8437C3D8-7689-4200-BF38-79E4AC33DFA0,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 8437C3D8-7689-4200-BF38-79E4AC33DFA0
distinguishedName: CN=8437C3D8-7689-4200-BF38-79E4AC33DFA0,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5772
uSNChanged: 5772
showInAdvancedViewOnly: TRUE
name: 8437C3D8-7689-4200-BF38-79E4AC33DFA0
objectGUID:: t1tLoKah20qH+j5PY9/D0Q==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 7cfb016c-4f87-4406-8166-bd9df943947f, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=7cfb016c-4f87-4406-8166-bd9df943947f,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 7cfb016c-4f87-4406-8166-bd9df943947f
distinguishedName: CN=7cfb016c-4f87-4406-8166-bd9df943947f,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5773
uSNChanged: 5773
showInAdvancedViewOnly: TRUE
name: 7cfb016c-4f87-4406-8166-bd9df943947f
objectGUID:: qRisksftgUujxtgz4cLncg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# f7ed4553-d82b-49ef-a839-2f38a36bb069, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=f7ed4553-d82b-49ef-a839-2f38a36bb069,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: f7ed4553-d82b-49ef-a839-2f38a36bb069
distinguishedName: CN=f7ed4553-d82b-49ef-a839-2f38a36bb069,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5774
uSNChanged: 5774
showInAdvancedViewOnly: TRUE
name: f7ed4553-d82b-49ef-a839-2f38a36bb069
objectGUID:: hqqOb0vprkq/jbDiWFwBBA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 8ca38317-13a4-4bd4-806f-ebed6acb5d0c, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=8ca38317-13a4-4bd4-806f-ebed6acb5d0c,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 8ca38317-13a4-4bd4-806f-ebed6acb5d0c
distinguishedName: CN=8ca38317-13a4-4bd4-806f-ebed6acb5d0c,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5775
uSNChanged: 5775
showInAdvancedViewOnly: TRUE
name: 8ca38317-13a4-4bd4-806f-ebed6acb5d0c
objectGUID:: OA+x+YU+eEijeuL2Kz0wCw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 3c784009-1f57-4e2a-9b04-6915c9e71961, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=3c784009-1f57-4e2a-9b04-6915c9e71961,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 3c784009-1f57-4e2a-9b04-6915c9e71961
distinguishedName: CN=3c784009-1f57-4e2a-9b04-6915c9e71961,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5776
uSNChanged: 5776
showInAdvancedViewOnly: TRUE
name: 3c784009-1f57-4e2a-9b04-6915c9e71961
objectGUID:: lQZ2WJwPak2nKQqOlSA0pg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5678-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5678-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5678-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5678-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5777
uSNChanged: 5777
showInAdvancedViewOnly: TRUE
name: 6bcd5678-8314-11d6-977b-00c04f613221
objectGUID:: GZuLXxrMjES7zOBucDvYDQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5679-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5679-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5679-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5679-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5778
uSNChanged: 5778
showInAdvancedViewOnly: TRUE
name: 6bcd5679-8314-11d6-977b-00c04f613221
objectGUID:: LuqA2OHdOEaSk3Qpz3N42g==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd567a-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd567a-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd567a-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd567a-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5779
uSNChanged: 5779
showInAdvancedViewOnly: TRUE
name: 6bcd567a-8314-11d6-977b-00c04f613221
objectGUID:: YFTTo10GZEmJc6ZcOFv7Qw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd567b-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd567b-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd567b-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd567b-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5780
uSNChanged: 5780
showInAdvancedViewOnly: TRUE
name: 6bcd567b-8314-11d6-977b-00c04f613221
objectGUID:: u9ieYqJ9ckmF/mNh58bbOA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd567c-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd567c-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd567c-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd567c-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5781
uSNChanged: 5781
showInAdvancedViewOnly: TRUE
name: 6bcd567c-8314-11d6-977b-00c04f613221
objectGUID:: zqd9MoPF7E+c8PwxJX1hMQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd567d-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd567d-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd567d-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd567d-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5782
uSNChanged: 5782
showInAdvancedViewOnly: TRUE
name: 6bcd567d-8314-11d6-977b-00c04f613221
objectGUID:: 5Tuem03hmUu0fU1CMMaebw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd567e-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd567e-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd567e-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd567e-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5783
uSNChanged: 5783
showInAdvancedViewOnly: TRUE
name: 6bcd567e-8314-11d6-977b-00c04f613221
objectGUID:: FyQcoUIYY0CWkBNUVxe93A==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd567f-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd567f-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd567f-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd567f-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5784
uSNChanged: 5784
showInAdvancedViewOnly: TRUE
name: 6bcd567f-8314-11d6-977b-00c04f613221
objectGUID:: KxxJr/xp40uxr56oasa8tw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5680-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5680-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5680-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5680-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5785
uSNChanged: 5785
showInAdvancedViewOnly: TRUE
name: 6bcd5680-8314-11d6-977b-00c04f613221
objectGUID:: pbjcs0895kCcB0Chl65ODA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5681-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5681-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5681-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5681-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5786
uSNChanged: 5786
showInAdvancedViewOnly: TRUE
name: 6bcd5681-8314-11d6-977b-00c04f613221
objectGUID:: bBqVMd4OBEOYnS/CHur5Mg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5682-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5682-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5682-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5682-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5787
uSNChanged: 5787
showInAdvancedViewOnly: TRUE
name: 6bcd5682-8314-11d6-977b-00c04f613221
objectGUID:: aJDvrZALFUSc/bbQ7zQnTA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5683-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5683-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5683-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5683-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5788
uSNChanged: 5788
showInAdvancedViewOnly: TRUE
name: 6bcd5683-8314-11d6-977b-00c04f613221
objectGUID:: VCrPElGIHEOVcE9LvKN8IQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5684-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5684-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5684-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5684-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5789
uSNChanged: 5789
showInAdvancedViewOnly: TRUE
name: 6bcd5684-8314-11d6-977b-00c04f613221
objectGUID:: l6165lg1SU6FYkaWhRITiw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5685-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5685-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5685-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5685-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5790
uSNChanged: 5790
showInAdvancedViewOnly: TRUE
name: 6bcd5685-8314-11d6-977b-00c04f613221
objectGUID:: 2XN8Qy6XPkaubZ0HkZw4Qw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5686-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5686-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5686-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5686-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5791
uSNChanged: 5791
showInAdvancedViewOnly: TRUE
name: 6bcd5686-8314-11d6-977b-00c04f613221
objectGUID:: RF0y+2w6jUO9P0vcBAKGyQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5687-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5687-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5687-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5687-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5792
uSNChanged: 5792
showInAdvancedViewOnly: TRUE
name: 6bcd5687-8314-11d6-977b-00c04f613221
objectGUID:: 2bmjIDCHmUCu+49vjv14Ug==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5688-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5688-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5688-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5688-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5793
uSNChanged: 5793
showInAdvancedViewOnly: TRUE
name: 6bcd5688-8314-11d6-977b-00c04f613221
objectGUID:: Wb9IhKXAi0Ce8QFnDPyDAA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd5689-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd5689-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd5689-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd5689-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5794
uSNChanged: 5794
showInAdvancedViewOnly: TRUE
name: 6bcd5689-8314-11d6-977b-00c04f613221
objectGUID:: O7exn8buGke+pr0/zMS4HQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd568a-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd568a-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd568a-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd568a-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5795
uSNChanged: 5795
showInAdvancedViewOnly: TRUE
name: 6bcd568a-8314-11d6-977b-00c04f613221
objectGUID:: pFvgoTXvCUu49c9l53q8sQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd568b-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd568b-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd568b-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd568b-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5796
uSNChanged: 5796
showInAdvancedViewOnly: TRUE
name: 6bcd568b-8314-11d6-977b-00c04f613221
objectGUID:: Ac9iUr6rcUC0qwTrkZR9xg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd568c-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd568c-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd568c-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd568c-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5797
uSNChanged: 5797
showInAdvancedViewOnly: TRUE
name: 6bcd568c-8314-11d6-977b-00c04f613221
objectGUID:: wcuFMJSwP0eOqmKaAD6Zbw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 6bcd568d-8314-11d6-977b-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6bcd568d-8314-11d6-977b-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6bcd568d-8314-11d6-977b-00c04f613221
distinguishedName: CN=6bcd568d-8314-11d6-977b-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5798
uSNChanged: 5798
showInAdvancedViewOnly: TRUE
name: 6bcd568d-8314-11d6-977b-00c04f613221
objectGUID:: /9jDaUj+PU2iBCBMz6hooA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 3051c66f-b332-4a73-9a20-2d6a7d6e6a1c, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=3051c66f-b332-4a73-9a20-2d6a7d6e6a1c,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 3051c66f-b332-4a73-9a20-2d6a7d6e6a1c
distinguishedName: CN=3051c66f-b332-4a73-9a20-2d6a7d6e6a1c,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5799
uSNChanged: 5799
showInAdvancedViewOnly: TRUE
name: 3051c66f-b332-4a73-9a20-2d6a7d6e6a1c
objectGUID:: cci28jGImEOMsS0j9nIaSQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 3e4f4182-ac5d-4378-b760-0eab2de593e2, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=3e4f4182-ac5d-4378-b760-0eab2de593e2,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 3e4f4182-ac5d-4378-b760-0eab2de593e2
distinguishedName: CN=3e4f4182-ac5d-4378-b760-0eab2de593e2,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5800
uSNChanged: 5800
showInAdvancedViewOnly: TRUE
name: 3e4f4182-ac5d-4378-b760-0eab2de593e2
objectGUID:: Cju/Hq9ku0y9TGVc93wc6g==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# c4f17608-e611-11d6-9793-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=c4f17608-e611-11d6-9793-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: c4f17608-e611-11d6-9793-00c04f613221
distinguishedName: CN=c4f17608-e611-11d6-9793-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5801
uSNChanged: 5801
showInAdvancedViewOnly: TRUE
name: c4f17608-e611-11d6-9793-00c04f613221
objectGUID:: cJJ5BO9v2UuZYG4DmYUzrg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 13d15cf0-e6c8-11d6-9793-00c04f613221, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=13d15cf0-e6c8-11d6-9793-00c04f613221,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 13d15cf0-e6c8-11d6-9793-00c04f613221
distinguishedName: CN=13d15cf0-e6c8-11d6-9793-00c04f613221,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5802
uSNChanged: 5802
showInAdvancedViewOnly: TRUE
name: 13d15cf0-e6c8-11d6-9793-00c04f613221
objectGUID:: Qf+nkt2TrUSDlmh31fvU+w==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c
distinguishedName: CN=8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5803
uSNChanged: 5803
showInAdvancedViewOnly: TRUE
name: 8ddf6913-1c7b-4c59-a5af-b9ca3b3d2c4c
objectGUID:: jHt4/Bn+00yTRi+b63tmGw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# dda1d01d-4bd7-4c49-a184-46f9241b560e, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=dda1d01d-4bd7-4c49-a184-46f9241b560e,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: dda1d01d-4bd7-4c49-a184-46f9241b560e
distinguishedName: CN=dda1d01d-4bd7-4c49-a184-46f9241b560e,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5804
uSNChanged: 5804
showInAdvancedViewOnly: TRUE
name: dda1d01d-4bd7-4c49-a184-46f9241b560e
objectGUID:: LkdomJKATk6d6h+mYK9BwQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# a1789bfb-e0a2-4739-8cc0-e77d892d080a, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=a1789bfb-e0a2-4739-8cc0-e77d892d080a,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: a1789bfb-e0a2-4739-8cc0-e77d892d080a
distinguishedName: CN=a1789bfb-e0a2-4739-8cc0-e77d892d080a,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5805
uSNChanged: 5805
showInAdvancedViewOnly: TRUE
name: a1789bfb-e0a2-4739-8cc0-e77d892d080a
objectGUID:: SYdVY/wwCUKw9RbVYPr65g==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 61b34cb0-55ee-4be9-b595-97810b92b017, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=61b34cb0-55ee-4be9-b595-97810b92b017,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 61b34cb0-55ee-4be9-b595-97810b92b017
distinguishedName: CN=61b34cb0-55ee-4be9-b595-97810b92b017,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5806
uSNChanged: 5806
showInAdvancedViewOnly: TRUE
name: 61b34cb0-55ee-4be9-b595-97810b92b017
objectGUID:: GDkkKhVpOE+OlV2ig+QpvQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 57428d75-bef7-43e1-938b-2e749f5a8d56, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=57428d75-bef7-43e1-938b-2e749f5a8d56,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 57428d75-bef7-43e1-938b-2e749f5a8d56
distinguishedName: CN=57428d75-bef7-43e1-938b-2e749f5a8d56,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5807
uSNChanged: 5807
showInAdvancedViewOnly: TRUE
name: 57428d75-bef7-43e1-938b-2e749f5a8d56
objectGUID:: viEYFy9z8kGXmBNvFgDwaQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# ebad865a-d649-416f-9922-456b53bbb5b8, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=ebad865a-d649-416f-9922-456b53bbb5b8,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: ebad865a-d649-416f-9922-456b53bbb5b8
distinguishedName: CN=ebad865a-d649-416f-9922-456b53bbb5b8,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5808
uSNChanged: 5808
showInAdvancedViewOnly: TRUE
name: ebad865a-d649-416f-9922-456b53bbb5b8
objectGUID:: +m8N3CgL3EahZLGcHLfI7A==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 0b7fb422-3609-4587-8c2e-94b10f67d1bf, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=0b7fb422-3609-4587-8c2e-94b10f67d1bf,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 0b7fb422-3609-4587-8c2e-94b10f67d1bf
distinguishedName: CN=0b7fb422-3609-4587-8c2e-94b10f67d1bf,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5809
uSNChanged: 5809
showInAdvancedViewOnly: TRUE
name: 0b7fb422-3609-4587-8c2e-94b10f67d1bf
objectGUID:: q98x8bnirEWitSjMGOXcEg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 2951353e-d102-4ea5-906c-54247eeec741, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=2951353e-d102-4ea5-906c-54247eeec741,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 2951353e-d102-4ea5-906c-54247eeec741
distinguishedName: CN=2951353e-d102-4ea5-906c-54247eeec741,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5810
uSNChanged: 5810
showInAdvancedViewOnly: TRUE
name: 2951353e-d102-4ea5-906c-54247eeec741
objectGUID:: yIYtRQu3dEqR8pfzznajyQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 71482d49-8870-4cb3-a438-b6fc9ec35d70, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=71482d49-8870-4cb3-a438-b6fc9ec35d70,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 71482d49-8870-4cb3-a438-b6fc9ec35d70
distinguishedName: CN=71482d49-8870-4cb3-a438-b6fc9ec35d70,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5811
uSNChanged: 5811
showInAdvancedViewOnly: TRUE
name: 71482d49-8870-4cb3-a438-b6fc9ec35d70
objectGUID:: LPlmy02dX0in5W5BdmkrXA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# aed72870-bf16-4788-8ac7-22299c8207f1, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=aed72870-bf16-4788-8ac7-22299c8207f1,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: aed72870-bf16-4788-8ac7-22299c8207f1
distinguishedName: CN=aed72870-bf16-4788-8ac7-22299c8207f1,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5812
uSNChanged: 5812
showInAdvancedViewOnly: TRUE
name: aed72870-bf16-4788-8ac7-22299c8207f1
objectGUID:: mGG3tFdmdkGexvCLUVxYjg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# f58300d1-b71a-4DB6-88a1-a8b9538beaca, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=f58300d1-b71a-4DB6-88a1-a8b9538beaca,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: f58300d1-b71a-4DB6-88a1-a8b9538beaca
distinguishedName: CN=f58300d1-b71a-4DB6-88a1-a8b9538beaca,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5813
uSNChanged: 5813
showInAdvancedViewOnly: TRUE
name: f58300d1-b71a-4DB6-88a1-a8b9538beaca
objectGUID:: gnO1eX54SU6dvQyjB5XDsg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 231fb90b-c92a-40c9-9379-bacfc313a3e3, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=231fb90b-c92a-40c9-9379-bacfc313a3e3,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 231fb90b-c92a-40c9-9379-bacfc313a3e3
distinguishedName: CN=231fb90b-c92a-40c9-9379-bacfc313a3e3,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5814
uSNChanged: 5814
showInAdvancedViewOnly: TRUE
name: 231fb90b-c92a-40c9-9379-bacfc313a3e3
objectGUID:: 0X9W1aqMmUCn59t5/i+3xA==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0
distinguishedName: CN=4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5815
uSNChanged: 5815
showInAdvancedViewOnly: TRUE
name: 4aaabc3a-c416-4b9c-a6bb-4b453ab1c1f0
objectGUID:: LE2N9RPAPkO+ex+jItInmw==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 9738c400-7795-4d6e-b19d-c16cd6486166, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=9738c400-7795-4d6e-b19d-c16cd6486166,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 9738c400-7795-4d6e-b19d-c16cd6486166
distinguishedName: CN=9738c400-7795-4d6e-b19d-c16cd6486166,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5816
uSNChanged: 5816
showInAdvancedViewOnly: TRUE
name: 9738c400-7795-4d6e-b19d-c16cd6486166
objectGUID:: GTJNeEwNOUOhqlvqn/rnyg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# de10d491-909f-4fb0-9abb-4b7865c0fe80, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=de10d491-909f-4fb0-9abb-4b7865c0fe80,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: de10d491-909f-4fb0-9abb-4b7865c0fe80
distinguishedName: CN=de10d491-909f-4fb0-9abb-4b7865c0fe80,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5817
uSNChanged: 5817
showInAdvancedViewOnly: TRUE
name: de10d491-909f-4fb0-9abb-4b7865c0fe80
objectGUID:: XYJ8VVAr4Ei1vvmqJ/LRYQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# b96ed344-545a-4172-aa0c-68118202f125, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=b96ed344-545a-4172-aa0c-68118202f125,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: b96ed344-545a-4172-aa0c-68118202f125
distinguishedName: CN=b96ed344-545a-4172-aa0c-68118202f125,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5818
uSNChanged: 5818
showInAdvancedViewOnly: TRUE
name: b96ed344-545a-4172-aa0c-68118202f125
objectGUID:: qmfRw7qfOUeUpOQC/gfGjQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 4c93ad42-178a-4275-8600-16811d28f3aa, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=4c93ad42-178a-4275-8600-16811d28f3aa,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 4c93ad42-178a-4275-8600-16811d28f3aa
distinguishedName: CN=4c93ad42-178a-4275-8600-16811d28f3aa,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5819
uSNChanged: 5819
showInAdvancedViewOnly: TRUE
name: 4c93ad42-178a-4275-8600-16811d28f3aa
objectGUID:: I8qAZQURK02QgL7udj9Oqg==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# c88227bc-fcca-4b58-8d8a-cd3d64528a02, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=c88227bc-fcca-4b58-8d8a-cd3d64528a02,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: c88227bc-fcca-4b58-8d8a-cd3d64528a02
distinguishedName: CN=c88227bc-fcca-4b58-8d8a-cd3d64528a02,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5820
uSNChanged: 5820
showInAdvancedViewOnly: TRUE
name: c88227bc-fcca-4b58-8d8a-cd3d64528a02
objectGUID:: BPuUwvtMM0iwgHmwwM0U1w==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 5e1574f6-55df-493e-a671-aaeffca6a100, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=5e1574f6-55df-493e-a671-aaeffca6a100,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 5e1574f6-55df-493e-a671-aaeffca6a100
distinguishedName: CN=5e1574f6-55df-493e-a671-aaeffca6a100,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5821
uSNChanged: 5821
showInAdvancedViewOnly: TRUE
name: 5e1574f6-55df-493e-a671-aaeffca6a100
objectGUID:: CeXnUJZ5g0ebhrUrb19c/g==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# d262aae8-41f7-48ed-9f35-56bbb677573d, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=d262aae8-41f7-48ed-9f35-56bbb677573d,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: d262aae8-41f7-48ed-9f35-56bbb677573d
distinguishedName: CN=d262aae8-41f7-48ed-9f35-56bbb677573d,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5822
uSNChanged: 5822
showInAdvancedViewOnly: TRUE
name: d262aae8-41f7-48ed-9f35-56bbb677573d
objectGUID:: jO5KITo58EOQdqLfRbON3Q==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# 82112ba0-7e4c-4a44-89d9-d46c9612bf91, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=82112ba0-7e4c-4a44-89d9-d46c9612bf91,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 82112ba0-7e4c-4a44-89d9-d46c9612bf91
distinguishedName: CN=82112ba0-7e4c-4a44-89d9-d46c9612bf91,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5823
uSNChanged: 5823
showInAdvancedViewOnly: TRUE
name: 82112ba0-7e4c-4a44-89d9-d46c9612bf91
objectGUID:: P+NXz+NSR02FFeYv99AEtQ==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# Windows2003Update, DomainUpdates, System, active.htb
dn: CN=Windows2003Update,CN=DomainUpdates,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: Windows2003Update
distinguishedName: CN=Windows2003Update,CN=DomainUpdates,CN=System,DC=active,D
 C=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5824
uSNChanged: 5824
showInAdvancedViewOnly: TRUE
name: Windows2003Update
objectGUID:: k6LGhPir/0qMnb8tyrjMCA==
revision: 9
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# ActiveDirectoryUpdate, DomainUpdates, System, active.htb
dn: CN=ActiveDirectoryUpdate,CN=DomainUpdates,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: ActiveDirectoryUpdate
distinguishedName: CN=ActiveDirectoryUpdate,CN=DomainUpdates,CN=System,DC=acti
 ve,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5825
uSNChanged: 5825
showInAdvancedViewOnly: TRUE
name: ActiveDirectoryUpdate
objectGUID:: 1Svi3/gi7kCv1lavWicNyQ==
revision: 5
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# Password Settings Container, System, active.htb
dn: CN=Password Settings Container,CN=System,DC=active,DC=htb

# PSPs, System, active.htb
dn: CN=PSPs,CN=System,DC=active,DC=htb
objectClass: top
objectClass: container
objectClass: msImaging-PSPs
cn: PSPs
distinguishedName: CN=PSPs,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 5827
uSNChanged: 5827
name: PSPs
objectGUID:: VeTJd6Rt+kCCeFOvtzX56w==
objectCategory: CN=ms-Imaging-PSPs,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# Administrator, Users, active.htb
dn: CN=Administrator,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Administrator
description: Built-in account for administering the computer/domain
distinguishedName: CN=Administrator,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20220429152711.0Z
uSNCreated: 8196
memberOf: CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb
memberOf: CN=Domain Admins,CN=Users,DC=active,DC=htb
memberOf: CN=Enterprise Admins,CN=Users,DC=active,DC=htb
memberOf: CN=Schema Admins,CN=Users,DC=active,DC=htb
memberOf: CN=Administrators,CN=Builtin,DC=active,DC=htb
uSNChanged: 94244
name: Administrator
objectGUID:: jnHKJRJzf0aVWkxPEJY8Hg==
userAccountControl: 66048
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 131774446554773106
lastLogoff: 0
lastLogon: 132957196657333725
logonHours:: ////////////////////////////
pwdLastSet: 131764144003517228
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv129AEAAA==
adminCount: 1
accountExpires: 0
logonCount: 60
sAMAccountName: Administrator
sAMAccountType: 805306368
servicePrincipalName: active/CIFS:445
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718203435.0Z
dSCorePropagationData: 20180718201454.0Z
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z
lastLogonTimestamp: 132957196310233115
msDS-SupportedEncryptionTypes: 0

# Guest, Users, active.htb
dn: CN=Guest,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Guest
description: Built-in account for guest access to the computer/domain
distinguishedName: CN=Guest,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8197
memberOf: CN=Guests,CN=Builtin,DC=active,DC=htb
uSNChanged: 8197
name: Guest
objectGUID:: qTSHEg7/XE+MlaFHOKEYAQ==
userAccountControl: 66082
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 0
pwdLastSet: 0
primaryGroupID: 514
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv129QEAAA==
accountExpires: 9223372036854775807
logonCount: 0
sAMAccountName: Guest
sAMAccountType: 805306368
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Builtin, active.htb
dn: CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: builtinDomain
cn: Builtin
distinguishedName: CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8198
uSNChanged: 8198
showInAdvancedViewOnly: FALSE
name: Builtin
objectGUID:: jzW8rz+CWk60UL2d4o+lyw==
creationTime: 128920205740836625
forceLogoff: -9223372036854775808
lockoutDuration: -18000000000
lockOutObservationWindow: -18000000000
lockoutThreshold: 0
maxPwdAge: -37108517437440
minPwdAge: 0
minPwdLength: 0
modifiedCountAtLastProm: 0
nextRid: 1000
pwdProperties: 0
pwdHistoryLength: 0
objectSid:: AQEAAAAAAAUgAAAA
serverState: 1
uASCompat: 1
modifiedCount: 87
systemFlags: -1946157056
objectCategory: CN=Builtin-Domain,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Administrators, Builtin, active.htb
dn: CN=Administrators,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Administrators
description: Administrators have complete and unrestricted access to the compu
 ter/domain
member: CN=Domain Admins,CN=Users,DC=active,DC=htb
member: CN=Enterprise Admins,CN=Users,DC=active,DC=htb
member: CN=Administrator,CN=Users,DC=active,DC=htb
distinguishedName: CN=Administrators,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 8199
uSNChanged: 12731
name: Administrators
objectGUID:: 0lUkN/t/iUqZE5TocnFF4w==
objectSid:: AQIAAAAAAAUgAAAAIAIAAA==
adminCount: 1
sAMAccountName: Administrators
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Users, Builtin, active.htb
dn: CN=Users,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Users
description: Users are prevented from making accidental or intentional system-
 wide changes and can run most applications
member: CN=Domain Users,CN=Users,DC=active,DC=htb
member: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=active,DC=htb
member: CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=active,DC=htb
distinguishedName: CN=Users,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 8202
uSNChanged: 12381
name: Users
objectGUID:: qe3hfyF0sEqoV6oOQ7MVUw==
objectSid:: AQIAAAAAAAUgAAAAIQIAAA==
sAMAccountName: Users
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# S-1-5-4, ForeignSecurityPrincipals, active.htb
dn: CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=active,DC=htb
objectClass: top
objectClass: foreignSecurityPrincipal
cn: S-1-5-4
distinguishedName: CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=active,DC=htb
showInAdvancedViewOnly: TRUE
name: S-1-5-4
objectGUID:: hp/S09aB9UKLVSzJGZwn5Q==
objectSid:: AQEAAAAAAAUEAAAA
objectCategory: CN=Foreign-Security-Principal,CN=Schema,CN=Configuration,DC=ac
 tive,DC=htb

# S-1-5-11, ForeignSecurityPrincipals, active.htb
dn: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=active,DC=htb
objectClass: top
objectClass: foreignSecurityPrincipal
cn: S-1-5-11
distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8204
memberOf: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=active,DC=htb
memberOf: CN=Users,CN=Builtin,DC=active,DC=htb
uSNChanged: 8204
showInAdvancedViewOnly: TRUE
name: S-1-5-11
objectGUID:: LuJjrR2d50+7tHJwQjfMJQ==
objectSid:: AQEAAAAAAAULAAAA
objectCategory: CN=Foreign-Security-Principal,CN=Schema,CN=Configuration,DC=ac
 tive,DC=htb
dSCorePropagationData: 16010101000000.0Z

# Guests, Builtin, active.htb
dn: CN=Guests,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Guests
description: Guests have the same access as members of the Users group by defa
 ult, except for the Guest account which is further restricted
member: CN=Domain Guests,CN=Users,DC=active,DC=htb
member: CN=Guest,CN=Users,DC=active,DC=htb
distinguishedName: CN=Guests,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 8208
uSNChanged: 12383
name: Guests
objectGUID:: ci/G/4gWSkG4vnoj86O6vw==
objectSid:: AQIAAAAAAAUgAAAAIgIAAA==
sAMAccountName: Guests
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Print Operators, Builtin, active.htb
dn: CN=Print Operators,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Print Operators
description: Members can administer domain printers
distinguishedName: CN=Print Operators,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 8211
uSNChanged: 12736
name: Print Operators
objectGUID:: 7JwzKgWyiku8yxfVnTZuEg==
objectSid:: AQIAAAAAAAUgAAAAJgIAAA==
adminCount: 1
sAMAccountName: Print Operators
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Backup Operators, Builtin, active.htb
dn: CN=Backup Operators,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Backup Operators
description: Backup Operators can override security restrictions for the sole 
 purpose of backing up or restoring files
distinguishedName: CN=Backup Operators,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 8212
uSNChanged: 12733
name: Backup Operators
objectGUID:: 3kGxr/YSzUq0LZpQrIFYxA==
objectSid:: AQIAAAAAAAUgAAAAJwIAAA==
adminCount: 1
sAMAccountName: Backup Operators
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Replicator, Builtin, active.htb
dn: CN=Replicator,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Replicator
description: Supports file replication in a domain
distinguishedName: CN=Replicator,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 8213
uSNChanged: 12729
name: Replicator
objectGUID:: aTBtXU7OTEygP/Vwre/QJw==
objectSid:: AQIAAAAAAAUgAAAAKAIAAA==
adminCount: 1
sAMAccountName: Replicator
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Remote Desktop Users, Builtin, active.htb
dn: CN=Remote Desktop Users,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Remote Desktop Users
description: Members in this group are granted the right to logon remotely
distinguishedName: CN=Remote Desktop Users,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8214
uSNChanged: 8214
name: Remote Desktop Users
objectGUID:: 9yRXmmTj30C5RPT+oW0qcw==
objectSid:: AQIAAAAAAAUgAAAAKwIAAA==
sAMAccountName: Remote Desktop Users
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Network Configuration Operators, Builtin, active.htb
dn: CN=Network Configuration Operators,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Network Configuration Operators
description: Members in this group can have some administrative privileges to 
 manage configuration of networking features
distinguishedName: CN=Network Configuration Operators,CN=Builtin,DC=active,DC=
 htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8215
uSNChanged: 8215
name: Network Configuration Operators
objectGUID:: rmKORdJ6kEiNjqwSHUNEQw==
objectSid:: AQIAAAAAAAUgAAAALAIAAA==
sAMAccountName: Network Configuration Operators
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Performance Monitor Users, Builtin, active.htb
dn: CN=Performance Monitor Users,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Performance Monitor Users
description: Members of this group can access performance counter data locally
  and remotely
distinguishedName: CN=Performance Monitor Users,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8216
uSNChanged: 8216
name: Performance Monitor Users
objectGUID:: THDcZb35AEuK+vHewmjPgA==
objectSid:: AQIAAAAAAAUgAAAALgIAAA==
sAMAccountName: Performance Monitor Users
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Performance Log Users, Builtin, active.htb
dn: CN=Performance Log Users,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Performance Log Users
description: Members of this group may schedule logging of performance counter
 s, enable trace providers, and collect event traces both locally and via remo
 te access to this computer
distinguishedName: CN=Performance Log Users,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8217
uSNChanged: 8217
name: Performance Log Users
objectGUID:: gX6ORLss2Ee3o7zEFWxOuA==
objectSid:: AQIAAAAAAAUgAAAALwIAAA==
sAMAccountName: Performance Log Users
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Distributed COM Users, Builtin, active.htb
dn: CN=Distributed COM Users,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Distributed COM Users
description: Members are allowed to launch, activate and use Distributed COM o
 bjects on this machine.
distinguishedName: CN=Distributed COM Users,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8218
uSNChanged: 8218
name: Distributed COM Users
objectGUID:: 5Egw/C/9H0qw6pzG6UQcZw==
objectSid:: AQIAAAAAAAUgAAAAMgIAAA==
sAMAccountName: Distributed COM Users
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# IIS_IUSRS, Builtin, active.htb
dn: CN=IIS_IUSRS,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: IIS_IUSRS
description: Built-in group used by Internet Information Services.
member: CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=active,DC=htb
distinguishedName: CN=IIS_IUSRS,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8219
uSNChanged: 8222
name: IIS_IUSRS
objectGUID:: 4cB9wvUHVUWwemS51kM3cg==
objectSid:: AQIAAAAAAAUgAAAAOAIAAA==
sAMAccountName: IIS_IUSRS
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# S-1-5-17, ForeignSecurityPrincipals, active.htb
dn: CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=active,DC=htb
objectClass: top
objectClass: foreignSecurityPrincipal
cn: S-1-5-17
distinguishedName: CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=active,DC=htb
showInAdvancedViewOnly: TRUE
name: S-1-5-17
objectGUID:: zsOAOXqL7E2vwax86biXIA==
objectSid:: AQEAAAAAAAURAAAA
objectCategory: CN=Foreign-Security-Principal,CN=Schema,CN=Configuration,DC=ac
 tive,DC=htb

# Cryptographic Operators, Builtin, active.htb
dn: CN=Cryptographic Operators,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Cryptographic Operators
description: Members are authorized to perform cryptographic operations.
distinguishedName: CN=Cryptographic Operators,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8223
uSNChanged: 8223
name: Cryptographic Operators
objectGUID:: uKDGLcrtekyLr24q107ltg==
objectSid:: AQIAAAAAAAUgAAAAOQIAAA==
sAMAccountName: Cryptographic Operators
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Event Log Readers, Builtin, active.htb
dn: CN=Event Log Readers,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Event Log Readers
description: Members of this group can read event logs from local machine
distinguishedName: CN=Event Log Readers,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8224
uSNChanged: 8224
name: Event Log Readers
objectGUID:: pe3htEkX9EaG3U3iar/xhQ==
objectSid:: AQIAAAAAAAUgAAAAPQIAAA==
sAMAccountName: Event Log Readers
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Certificate Service DCOM Access, Builtin, active.htb
dn: CN=Certificate Service DCOM Access,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Certificate Service DCOM Access
description: Members of this group are allowed to connect to Certification Aut
 horities in the enterprise
distinguishedName: CN=Certificate Service DCOM Access,CN=Builtin,DC=active,DC=
 htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718184911.0Z
uSNCreated: 8225
uSNChanged: 8225
name: Certificate Service DCOM Access
objectGUID:: ZLLQbjZAv0uQwDSgjmpJ0w==
objectSid:: AQIAAAAAAAUgAAAAPgIAAA==
sAMAccountName: Certificate Service DCOM Access
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Server, System, active.htb
dn: CN=Server,CN=System,DC=active,DC=htb
objectClass: top
objectClass: securityObject
objectClass: samServer
cn: Server
distinguishedName: CN=Server,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718184911.0Z
whenChanged: 20180718185537.0Z
uSNCreated: 8226
uSNChanged: 12693
showInAdvancedViewOnly: TRUE
name: Server
objectGUID:: VSvkRiZqgkCI5/yff94iVg==
revision: 65543
systemFlags: -1946157056
objectCategory: CN=Sam-Server,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z
samDomainUpdates:: /gE=

# DC, Domain Controllers, active.htb
dn: CN=DC,OU=Domain Controllers,DC=active,DC=htb
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
objectClass: computer
cn: DC
distinguishedName: CN=DC,OU=Domain Controllers,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185035.0Z
whenChanged: 20220429152658.0Z
uSNCreated: 12293
uSNChanged: 94237
name: DC
objectGUID:: 8+IJCvv15EeIY91yEStv/Q==
userAccountControl: 532480
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 132957196225056966
localPolicyFlags: 0
pwdLastSet: 132957196126776793
primaryGroupID: 516
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv126AMAAA==
accountExpires: 9223372036854775807
logonCount: 101
sAMAccountName: DC$
sAMAccountType: 805306369
operatingSystem: Windows Server 2008 R2 Standard
operatingSystemVersion: 6.1 (7601)
operatingSystemServicePack: Service Pack 1
serverReferenceBL: CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Con
 figuration,DC=active,DC=htb
dNSHostName: DC.active.htb
rIDSetReferences: CN=RID Set,CN=DC,OU=Domain Controllers,DC=active,DC=htb
servicePrincipalName: ldap/DC.active.htb/ForestDnsZones.active.htb
servicePrincipalName: ldap/DC.active.htb/DomainDnsZones.active.htb
servicePrincipalName: TERMSRV/DC
servicePrincipalName: TERMSRV/DC.active.htb
servicePrincipalName: Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/DC.active.htb
servicePrincipalName: DNS/DC.active.htb
servicePrincipalName: GC/DC.active.htb/active.htb
servicePrincipalName: RestrictedKrbHost/DC.active.htb
servicePrincipalName: RestrictedKrbHost/DC
servicePrincipalName: HOST/DC/ACTIVE
servicePrincipalName: HOST/DC.active.htb/ACTIVE
servicePrincipalName: HOST/DC
servicePrincipalName: HOST/DC.active.htb
servicePrincipalName: HOST/DC.active.htb/active.htb
servicePrincipalName: E3514235-4B06-11D1-AB04-00C04FC2DCD2/f4953ea5-0f30-4041-
 b4dd-1a00693a8510/active.htb
servicePrincipalName: ldap/DC/ACTIVE
servicePrincipalName: ldap/f4953ea5-0f30-4041-b4dd-1a00693a8510._msdcs.active.
 htb
servicePrincipalName: ldap/DC.active.htb/ACTIVE
servicePrincipalName: ldap/DC
servicePrincipalName: ldap/DC.active.htb
servicePrincipalName: ldap/DC.active.htb/active.htb
objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z
lastLogonTimestamp: 132957196185588896
msDS-SupportedEncryptionTypes: 31
msDFSR-ComputerReferenceBL: CN=DC,CN=Topology,CN=Domain System Volume,CN=DFSR-
 GlobalSettings,CN=System,DC=active,DC=htb

# krbtgt, Users, active.htb
dn: CN=krbtgt,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: krbtgt
description: Key Distribution Center Service Account
distinguishedName: CN=krbtgt,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185035.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 12324
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
uSNChanged: 12739
showInAdvancedViewOnly: TRUE
name: krbtgt
objectGUID:: 56HXQ6alq0mC0OJOdHL4jQ==
userAccountControl: 514
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 0
pwdLastSet: 131764134369720307
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv129gEAAA==
adminCount: 1
accountExpires: 9223372036854775807
logonCount: 0
sAMAccountName: krbtgt
sAMAccountType: 805306368
servicePrincipalName: kadmin/changepw
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Domain Computers, Users, active.htb
dn: CN=Domain Computers,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Domain Computers
description: All workstations and servers joined to the domain
distinguishedName: CN=Domain Computers,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12330
uSNChanged: 12332
name: Domain Computers
objectGUID:: eA+MXtYFrU633cqRR7Xl3g==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12AwIAAA==
sAMAccountName: Domain Computers
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Domain Controllers, Users, active.htb
dn: CN=Domain Controllers,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Domain Controllers
description: All domain controllers in the domain
distinguishedName: CN=Domain Controllers,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 12333
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
uSNChanged: 12741
name: Domain Controllers
objectGUID:: WcBWK0jsFkWhH4rSiOiP8w==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12BAIAAA==
adminCount: 1
sAMAccountName: Domain Controllers
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Schema Admins, Users, active.htb
dn: CN=Schema Admins,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Schema Admins
description: Designated administrators of the schema
member: CN=Administrator,CN=Users,DC=active,DC=htb
distinguishedName: CN=Schema Admins,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 12336
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
uSNChanged: 12724
name: Schema Admins
objectGUID:: WxKO7TjU3Uy6LFP354N0Vw==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12BgIAAA==
adminCount: 1
sAMAccountName: Schema Admins
sAMAccountType: 268435456
groupType: -2147483640
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Enterprise Admins, Users, active.htb
dn: CN=Enterprise Admins,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Enterprise Admins
description: Designated administrators of the enterprise
member: CN=Administrator,CN=Users,DC=active,DC=htb
distinguishedName: CN=Enterprise Admins,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 12339
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
memberOf: CN=Administrators,CN=Builtin,DC=active,DC=htb
uSNChanged: 12727
name: Enterprise Admins
objectGUID:: wh3TqP/Qp0egxmQVMGF9lg==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12BwIAAA==
adminCount: 1
sAMAccountName: Enterprise Admins
sAMAccountType: 268435456
groupType: -2147483640
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Cert Publishers, Users, active.htb
dn: CN=Cert Publishers,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Cert Publishers
description: Members of this group are permitted to publish certificates to th
 e directory
distinguishedName: CN=Cert Publishers,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12342
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
uSNChanged: 12344
name: Cert Publishers
objectGUID:: GV5Y4oMYD0eV8Kt+w9DPVQ==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12BQIAAA==
sAMAccountName: Cert Publishers
sAMAccountType: 536870912
groupType: -2147483644
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Domain Admins, Users, active.htb
dn: CN=Domain Admins,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Domain Admins
description: Designated administrators of the domain
member: CN=Administrator,CN=Users,DC=active,DC=htb
distinguishedName: CN=Domain Admins,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 12345
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
memberOf: CN=Administrators,CN=Builtin,DC=active,DC=htb
uSNChanged: 12723
name: Domain Admins
objectGUID:: DHSBeiG1KEG/3FdFPnNZMg==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12AAIAAA==
adminCount: 1
sAMAccountName: Domain Admins
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Domain Users, Users, active.htb
dn: CN=Domain Users,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Domain Users
description: All domain users
distinguishedName: CN=Domain Users,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12348
memberOf: CN=Users,CN=Builtin,DC=active,DC=htb
uSNChanged: 12350
name: Domain Users
objectGUID:: V08rHi6B9k6R8jEfaFjkAw==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12AQIAAA==
sAMAccountName: Domain Users
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Domain Guests, Users, active.htb
dn: CN=Domain Guests,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Domain Guests
description: All domain guests
distinguishedName: CN=Domain Guests,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12351
memberOf: CN=Guests,CN=Builtin,DC=active,DC=htb
uSNChanged: 12353
name: Domain Guests
objectGUID:: u6yOvOBclE+5USF3kntlXw==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12AgIAAA==
sAMAccountName: Domain Guests
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Group Policy Creator Owners, Users, active.htb
dn: CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Group Policy Creator Owners
description: Members in this group can modify group policy for the domain
member: CN=Administrator,CN=Users,DC=active,DC=htb
distinguishedName: CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12354
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
uSNChanged: 12391
name: Group Policy Creator Owners
objectGUID:: MhPwO3sl/0qIw+pBBFZMEQ==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12CAIAAA==
sAMAccountName: Group Policy Creator Owners
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# RAS and IAS Servers, Users, active.htb
dn: CN=RAS and IAS Servers,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: RAS and IAS Servers
description: Servers in this group can access remote access properties of user
 s
distinguishedName: CN=RAS and IAS Servers,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12357
uSNChanged: 12359
name: RAS and IAS Servers
objectGUID:: nG1B6R2MzE2TpNHVXoZMKw==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12KQIAAA==
sAMAccountName: RAS and IAS Servers
sAMAccountType: 536870912
groupType: -2147483644
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Server Operators, Builtin, active.htb
dn: CN=Server Operators,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Server Operators
description: Members can administer domain servers
distinguishedName: CN=Server Operators,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 12360
uSNChanged: 12737
name: Server Operators
objectGUID:: 8ZeTc4RhvUew3keWP81NVg==
objectSid:: AQIAAAAAAAUgAAAAJQIAAA==
adminCount: 1
sAMAccountName: Server Operators
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Account Operators, Builtin, active.htb
dn: CN=Account Operators,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Account Operators
description: Members can administer domain user and group accounts
distinguishedName: CN=Account Operators,CN=Builtin,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 12363
uSNChanged: 12734
name: Account Operators
objectGUID:: 6SEg1GYQlkiNYdveh7tKeg==
objectSid:: AQIAAAAAAAUgAAAAJAIAAA==
adminCount: 1
sAMAccountName: Account Operators
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Pre-Windows 2000 Compatible Access, Builtin, active.htb
dn: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Pre-Windows 2000 Compatible Access
description: A backward compatibility group which allows read access on all us
 ers and groups in the domain
member: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=active,DC=htb
distinguishedName: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=active,
 DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12366
uSNChanged: 12393
name: Pre-Windows 2000 Compatible Access
objectGUID:: 3terM+aIUUeXOzmdcfnKLA==
objectSid:: AQIAAAAAAAUgAAAAKgIAAA==
sAMAccountName: Pre-Windows 2000 Compatible Access
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Incoming Forest Trust Builders, Builtin, active.htb
dn: CN=Incoming Forest Trust Builders,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Incoming Forest Trust Builders
description: Members of this group can create incoming, one-way trusts to this
  forest
distinguishedName: CN=Incoming Forest Trust Builders,CN=Builtin,DC=active,DC=h
 tb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12369
uSNChanged: 12371
name: Incoming Forest Trust Builders
objectGUID:: AEWclX7eSU2rPTzcDSBUnw==
objectSid:: AQIAAAAAAAUgAAAALQIAAA==
sAMAccountName: Incoming Forest Trust Builders
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Windows Authorization Access Group, Builtin, active.htb
dn: CN=Windows Authorization Access Group,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Windows Authorization Access Group
description: Members of this group have access to the computed tokenGroupsGlob
 alAndUniversal attribute on User objects
member: CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=active,DC=htb
distinguishedName: CN=Windows Authorization Access Group,CN=Builtin,DC=active,
 DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12372
uSNChanged: 12396
name: Windows Authorization Access Group
objectGUID:: W+fV59JlgEWy+mkHV2Dfcg==
objectSid:: AQIAAAAAAAUgAAAAMAIAAA==
sAMAccountName: Windows Authorization Access Group
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Terminal Server License Servers, Builtin, active.htb
dn: CN=Terminal Server License Servers,CN=Builtin,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Terminal Server License Servers
description: Members of this group can update user accounts in Active Director
 y with information about license issuance, for the purpose of tracking and re
 porting TS Per User CAL usage
distinguishedName: CN=Terminal Server License Servers,CN=Builtin,DC=active,DC=
 htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12375
uSNChanged: 12377
name: Terminal Server License Servers
objectGUID:: jQBEkRGaSEuZYC5tUjqcTg==
objectSid:: AQIAAAAAAAUgAAAAMQIAAA==
sAMAccountName: Terminal Server License Servers
sAMAccountType: 536870912
systemFlags: -1946157056
groupType: -2147483643
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# S-1-5-9, ForeignSecurityPrincipals, active.htb
dn: CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=active,DC=htb
objectClass: top
objectClass: foreignSecurityPrincipal
cn: S-1-5-9
distinguishedName: CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=active,DC=htb
showInAdvancedViewOnly: TRUE
name: S-1-5-9
objectGUID:: auhhguWmbk2Um+UP+losGw==
objectSid:: AQEAAAAAAAUJAAAA
objectCategory: CN=Foreign-Security-Principal,CN=Schema,CN=Configuration,DC=ac
 tive,DC=htb

# 6E157EDF-4E72-4052-A82A-EC3F91021A22, Operations, DomainUpdates, System, acti
 ve.htb
dn: CN=6E157EDF-4E72-4052-A82A-EC3F91021A22,CN=Operations,CN=DomainUpdates,CN=
 System,DC=active,DC=htb
objectClass: top
objectClass: container
cn: 6E157EDF-4E72-4052-A82A-EC3F91021A22
distinguishedName: CN=6E157EDF-4E72-4052-A82A-EC3F91021A22,CN=Operations,CN=Do
 mainUpdates,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12397
uSNChanged: 12397
showInAdvancedViewOnly: TRUE
name: 6E157EDF-4E72-4052-A82A-EC3F91021A22
objectGUID:: 9dRbuhU+A0+1OCrUfBMg0Q==
objectCategory: CN=Container,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# Allowed RODC Password Replication Group, Users, active.htb
dn: CN=Allowed RODC Password Replication Group,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Allowed RODC Password Replication Group
description: Members in this group can have their passwords replicated to all 
 read-only domain controllers in the domain
distinguishedName: CN=Allowed RODC Password Replication Group,CN=Users,DC=acti
 ve,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12402
uSNChanged: 12404
name: Allowed RODC Password Replication Group
objectGUID:: gYDGcAxeiE2DghPeLmp3rw==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12OwIAAA==
sAMAccountName: Allowed RODC Password Replication Group
sAMAccountType: 536870912
groupType: -2147483644
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Denied RODC Password Replication Group, Users, active.htb
dn: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Denied RODC Password Replication Group
description: Members in this group cannot have their passwords replicated to a
 ny read-only domain controllers in the domain
member: CN=Read-only Domain Controllers,CN=Users,DC=active,DC=htb
member: CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb
member: CN=Domain Admins,CN=Users,DC=active,DC=htb
member: CN=Cert Publishers,CN=Users,DC=active,DC=htb
member: CN=Enterprise Admins,CN=Users,DC=active,DC=htb
member: CN=Schema Admins,CN=Users,DC=active,DC=htb
member: CN=Domain Controllers,CN=Users,DC=active,DC=htb
member: CN=krbtgt,CN=Users,DC=active,DC=htb
distinguishedName: CN=Denied RODC Password Replication Group,CN=Users,DC=activ
 e,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12405
uSNChanged: 12433
name: Denied RODC Password Replication Group
objectGUID:: Fsje76zWZEuuYAnXeQBFxw==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12PAIAAA==
sAMAccountName: Denied RODC Password Replication Group
sAMAccountType: 536870912
groupType: -2147483644
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# Read-only Domain Controllers, Users, active.htb
dn: CN=Read-only Domain Controllers,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Read-only Domain Controllers
description: Members of this group are Read-Only Domain Controllers in the dom
 ain
distinguishedName: CN=Read-only Domain Controllers,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718190545.0Z
uSNCreated: 12419
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=active,DC=htb
uSNChanged: 12740
name: Read-only Domain Controllers
objectGUID:: R+EflIGWRUKR2TBIDhsMBA==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12CQIAAA==
adminCount: 1
sAMAccountName: Read-only Domain Controllers
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 20180718190545.0Z
dSCorePropagationData: 16010101000000.0Z

# Enterprise Read-only Domain Controllers, Users, active.htb
dn: CN=Enterprise Read-only Domain Controllers,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: Enterprise Read-only Domain Controllers
description: Members of this group are Read-Only Domain Controllers in the ent
 erprise
distinguishedName: CN=Enterprise Read-only Domain Controllers,CN=Users,DC=acti
 ve,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12429
uSNChanged: 12431
name: Enterprise Read-only Domain Controllers
objectGUID:: sxs8qOUB7UuCyQ3PgPJxtA==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv128gEAAA==
sAMAccountName: Enterprise Read-only Domain Controllers
sAMAccountType: 268435456
groupType: -2147483640
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# RID Manager$, System, active.htb
dn: CN=RID Manager$,CN=System,DC=active,DC=htb
objectClass: top
objectClass: rIDManager
cn: RID Manager$
distinguishedName: CN=RID Manager$,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12440
uSNChanged: 12445
showInAdvancedViewOnly: TRUE
name: RID Manager$
objectGUID:: Yv6D1/RrlUmbCp4tR1pmag==
fSMORoleOwner: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN
 =Sites,CN=Configuration,DC=active,DC=htb
rIDAvailablePool: 4611686014132422208
systemFlags: -1946157056
objectCategory: CN=RID-Manager,CN=Schema,CN=Configuration,DC=active,DC=htb
isCriticalSystemObject: TRUE
dSCorePropagationData: 16010101000000.0Z

# RID Set, DC, Domain Controllers, active.htb
dn: CN=RID Set,CN=DC,OU=Domain Controllers,DC=active,DC=htb
objectClass: top
objectClass: rIDSet
cn: RID Set
distinguishedName: CN=RID Set,CN=DC,OU=Domain Controllers,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185037.0Z
whenChanged: 20180718185037.0Z
uSNCreated: 12443
uSNChanged: 12446
showInAdvancedViewOnly: TRUE
name: RID Set
objectGUID:: +3WSe2U0y0OE496JWz7CFg==
rIDAllocationPool: 6867652707404
rIDPreviousAllocationPool: 6867652707404
rIDUsedPool: 0
rIDNextRID: 1103
objectCategory: CN=RID-Set,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# DnsAdmins, Users, active.htb
dn: CN=DnsAdmins,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: DnsAdmins
description: DNS Administrators Group
distinguishedName: CN=DnsAdmins,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185115.0Z
whenChanged: 20180718185115.0Z
uSNCreated: 12456
uSNChanged: 12458
name: DnsAdmins
objectGUID:: lnE7LcWwZUiw4onP1fJ+HA==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12TQQAAA==
sAMAccountName: DnsAdmins
sAMAccountType: 536870912
groupType: -2147483644
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# DnsUpdateProxy, Users, active.htb
dn: CN=DnsUpdateProxy,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: group
cn: DnsUpdateProxy
description: DNS clients who are permitted to perform dynamic updates on behal
 f of some other clients (such as DHCP servers).
distinguishedName: CN=DnsUpdateProxy,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185115.0Z
whenChanged: 20180718185115.0Z
uSNCreated: 12461
uSNChanged: 12461
name: DnsUpdateProxy
objectGUID:: z4gyHIgQhUqWJ6Bs+Cc4nQ==
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12TgQAAA==
sAMAccountName: DnsUpdateProxy
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# MicrosoftDNS, System, active.htb
dn: CN=MicrosoftDNS,CN=System,DC=active,DC=htb

# RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=active,DC=htb
objectClass: top
objectClass: dnsZone
cn: Zone
distinguishedName: DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=active,DC=ht
 b
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12470
uSNChanged: 12472
showInAdvancedViewOnly: TRUE
name: RootDNSServers
objectGUID:: qwggHeoi1Euj60PfCgmNmA==
objectCategory: CN=Dns-Zone,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: RootDNSServers

# @, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=@,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=active,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=@,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=active,
 DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12473
uSNChanged: 12473
showInAdvancedViewOnly: TRUE
name: @
objectGUID:: D4evUlMUME2vnI6r1utlfg==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBbQxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBbAxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBawxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBagxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBaQxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBaAxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBZwxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBZgxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBZQxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBZAxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBYwxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBYgxyb290LXNlcnZlcnMDbmV0AA==
dnsRecord:: FgACAAUIAAAAAAAAAAAAAAAAAAAAAAAAFAMBYQxyb290LXNlcnZlcnMDbmV0AA==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: @

# a.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=a.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=a.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12474
uSNChanged: 12474
showInAdvancedViewOnly: TRUE
name: a.root-servers.net
objectGUID:: qaRiNZan8E+dakQxFOPlEA==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAxikABA==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: a.root-servers.net

# b.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=b.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=b.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12475
uSNChanged: 12475
showInAdvancedViewOnly: TRUE
name: b.root-servers.net
objectGUID:: mx6oac64Ekq84xtT+7maSg==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAwORPyQ==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: b.root-servers.net

# c.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=c.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=c.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12476
uSNChanged: 12476
showInAdvancedViewOnly: TRUE
name: c.root-servers.net
objectGUID:: aWhAqXjD/Ue3habKONnyig==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAwCEEDA==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: c.root-servers.net

# d.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=d.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=d.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12477
uSNChanged: 12477
showInAdvancedViewOnly: TRUE
name: d.root-servers.net
objectGUID:: qg3zrM7hs0+U7IulHOZEXw==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAgAgKWg==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: d.root-servers.net

# e.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=e.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=e.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12478
uSNChanged: 12478
showInAdvancedViewOnly: TRUE
name: e.root-servers.net
objectGUID:: zPCzM5fss0iRBE4CqFTXcA==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAwMvmCg==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: e.root-servers.net

# f.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=f.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=f.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12479
uSNChanged: 12479
showInAdvancedViewOnly: TRUE
name: f.root-servers.net
objectGUID:: N/ftEQCW406f/sFlzUbV3w==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAwAUF8Q==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: f.root-servers.net

# g.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=g.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=g.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12480
uSNChanged: 12480
showInAdvancedViewOnly: TRUE
name: g.root-servers.net
objectGUID:: nRd/2qaq2UmMQGwEGpzfOA==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAwHAkBA==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: g.root-servers.net

# h.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=h.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=h.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12481
uSNChanged: 12481
showInAdvancedViewOnly: TRUE
name: h.root-servers.net
objectGUID:: 3j/fHzRCF0ey7biQ8NIFKg==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAgD8CNQ==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: h.root-servers.net

# i.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=i.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=i.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12482
uSNChanged: 12482
showInAdvancedViewOnly: TRUE
name: i.root-servers.net
objectGUID:: vRKEuQ5gLkO3vC/LYHUbKw==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAwCSUEQ==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: i.root-servers.net

# j.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=j.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=j.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12483
uSNChanged: 12483
showInAdvancedViewOnly: TRUE
name: j.root-servers.net
objectGUID:: 6KCHCsQDwEWYh85G8RdEeQ==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAwDqAHg==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: j.root-servers.net

# k.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=k.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=k.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12484
uSNChanged: 12484
showInAdvancedViewOnly: TRUE
name: k.root-servers.net
objectGUID:: ilqCIavzH0u5o2Fc6l7ANw==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAwQAOgQ==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: k.root-servers.net

# l.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=l.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=l.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12485
uSNChanged: 12485
showInAdvancedViewOnly: TRUE
name: l.root-servers.net
objectGUID:: oV7YQR4gckCQl4+l4VehFQ==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAxwdTKg==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: l.root-servers.net

# m.root-servers.net, RootDNSServers, MicrosoftDNS, System, active.htb
dn: DC=m.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=System,DC=activ
 e,DC=htb
objectClass: top
objectClass: dnsNode
distinguishedName: DC=m.root-servers.net,DC=RootDNSServers,CN=MicrosoftDNS,CN=
 System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185116.0Z
whenChanged: 20180718185116.0Z
uSNCreated: 12486
uSNChanged: 12486
showInAdvancedViewOnly: TRUE
name: m.root-servers.net
objectGUID:: 4xKSz87xikWVpS0obB/xfg==
dnsRecord:: BAABAAUIAAAAAAAAAAAAAAAAAAAAAAAAygwbIQ==
objectCategory: CN=Dns-Node,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 20180718185116.0Z
dSCorePropagationData: 16010101000000.0Z
dc: m.root-servers.net

# DFSR-GlobalSettings, System, active.htb
dn: CN=DFSR-GlobalSettings,CN=System,DC=active,DC=htb
objectClass: top
objectClass: msDFSR-GlobalSettings
cn: DFSR-GlobalSettings
distinguishedName: CN=DFSR-GlobalSettings,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185122.0Z
whenChanged: 20180718185123.0Z
uSNCreated: 12521
uSNChanged: 12522
showInAdvancedViewOnly: TRUE
name: DFSR-GlobalSettings
objectGUID:: VaKZo4MpW0inkvScB+NOFQ==
objectCategory: CN=ms-DFSR-GlobalSettings,CN=Schema,CN=Configuration,DC=active
 ,DC=htb
dSCorePropagationData: 16010101000000.0Z
msDFSR-Flags: 48

# Domain System Volume, DFSR-GlobalSettings, System, active.htb
dn: CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=active,DC=htb
objectClass: top
objectClass: msDFSR-ReplicationGroup
cn: Domain System Volume
distinguishedName: CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC
 =active,DC=htb
instanceType: 4
whenCreated: 20180718185123.0Z
whenChanged: 20180718185123.0Z
uSNCreated: 12523
uSNChanged: 12523
showInAdvancedViewOnly: TRUE
name: Domain System Volume
objectGUID:: ag0jqthuHEejwTPI5XeWuA==
objectCategory: CN=ms-DFSR-ReplicationGroup,CN=Schema,CN=Configuration,DC=acti
 ve,DC=htb
dSCorePropagationData: 16010101000000.0Z
msDFSR-ReplicationGroupType: 1

# Content, Domain System Volume, DFSR-GlobalSettings, System, active.htb
dn: CN=Content,CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=act
 ive,DC=htb
objectClass: top
objectClass: msDFSR-Content
cn: Content
distinguishedName: CN=Content,CN=Domain System Volume,CN=DFSR-GlobalSettings,C
 N=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185123.0Z
whenChanged: 20180718185123.0Z
uSNCreated: 12524
uSNChanged: 12524
showInAdvancedViewOnly: TRUE
name: Content
objectGUID:: co0aolbJx0KOw0cP0KgmTg==
objectCategory: CN=ms-DFSR-Content,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z

# SYSVOL Share, Content, Domain System Volume, DFSR-GlobalSettings, System, act
 ive.htb
dn: CN=SYSVOL Share,CN=Content,CN=Domain System Volume,CN=DFSR-GlobalSettings,
 CN=System,DC=active,DC=htb
objectClass: top
objectClass: msDFSR-ContentSet
cn: SYSVOL Share
distinguishedName: CN=SYSVOL Share,CN=Content,CN=Domain System Volume,CN=DFSR-
 GlobalSettings,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185123.0Z
whenChanged: 20180718185123.0Z
uSNCreated: 12525
uSNChanged: 12525
showInAdvancedViewOnly: TRUE
name: SYSVOL Share
objectGUID:: aPos00Tz8Uy1XJMrqh8w+Q==
objectCategory: CN=ms-DFSR-ContentSet,CN=Schema,CN=Configuration,DC=active,DC=
 htb
dSCorePropagationData: 16010101000000.0Z
msDFSR-FileFilter: ~*,*.TMP,*.BAK
msDFSR-DirectoryFilter: DO_NOT_REMOVE_NtFrs_PreInstall_Directory,NtFrs_PreExis
 ting___See_EventLog

# Topology, Domain System Volume, DFSR-GlobalSettings, System, active.htb
dn: CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=ac
 tive,DC=htb
objectClass: top
objectClass: msDFSR-Topology
cn: Topology
distinguishedName: CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,
 CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185123.0Z
whenChanged: 20180718185123.0Z
uSNCreated: 12526
uSNChanged: 12526
showInAdvancedViewOnly: TRUE
name: Topology
objectGUID:: y+uAMobH6ka8Qlrcyt895A==
objectCategory: CN=ms-DFSR-Topology,CN=Schema,CN=Configuration,DC=active,DC=ht
 b
dSCorePropagationData: 16010101000000.0Z

# DC, Topology, Domain System Volume, DFSR-GlobalSettings, System, active.htb
dn: CN=DC,CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System
 ,DC=active,DC=htb
objectClass: top
objectClass: msDFSR-Member
cn: DC
distinguishedName: CN=DC,CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSet
 tings,CN=System,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185123.0Z
whenChanged: 20180718185123.0Z
uSNCreated: 12529
uSNChanged: 12529
showInAdvancedViewOnly: TRUE
name: DC
objectGUID:: 9V7DR4c9ikGiqrL1t4Qfug==
serverReference: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,
 CN=Sites,CN=Configuration,DC=active,DC=htb
objectCategory: CN=ms-DFSR-Member,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 16010101000000.0Z
msDFSR-ComputerReference: CN=DC,OU=Domain Controllers,DC=active,DC=htb
msDFSR-MemberReferenceBL: CN=Domain System Volume,CN=DFSR-LocalSettings,CN=DC,
 OU=Domain Controllers,DC=active,DC=htb

# DFSR-LocalSettings, DC, Domain Controllers, active.htb
dn: CN=DFSR-LocalSettings,CN=DC,OU=Domain Controllers,DC=active,DC=htb
objectClass: top
objectClass: msDFSR-LocalSettings
cn: DFSR-LocalSettings
distinguishedName: CN=DFSR-LocalSettings,CN=DC,OU=Domain Controllers,DC=active
 ,DC=htb
instanceType: 4
whenCreated: 20180718185123.0Z
whenChanged: 20180718185128.0Z
uSNCreated: 12530
uSNChanged: 12537
showInAdvancedViewOnly: TRUE
name: DFSR-LocalSettings
objectGUID:: 1TZp0RycLk2fD3QfawW4Dg==
objectCategory: CN=ms-DFSR-LocalSettings,CN=Schema,CN=Configuration,DC=active,
 DC=htb
dSCorePropagationData: 20180718185123.0Z
dSCorePropagationData: 16010101000000.0Z
msDFSR-Version: 1.0.0.0
msDFSR-Flags: 48

# Domain System Volume, DFSR-LocalSettings, DC, Domain Controllers, active.htb
dn: CN=Domain System Volume,CN=DFSR-LocalSettings,CN=DC,OU=Domain Controllers,
 DC=active,DC=htb
objectClass: top
objectClass: msDFSR-Subscriber
cn: Domain System Volume
distinguishedName: CN=Domain System Volume,CN=DFSR-LocalSettings,CN=DC,OU=Doma
 in Controllers,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185123.0Z
whenChanged: 20180718185123.0Z
uSNCreated: 12533
uSNChanged: 12533
showInAdvancedViewOnly: TRUE
name: Domain System Volume
objectGUID:: eCFb0z10kU+UAFWNJroSBw==
objectCategory: CN=ms-DFSR-Subscriber,CN=Schema,CN=Configuration,DC=active,DC=
 htb
dSCorePropagationData: 20180718185123.0Z
dSCorePropagationData: 16010101000000.0Z
msDFSR-ReplicationGroupGuid:: ag0jqthuHEejwTPI5XeWuA==
msDFSR-MemberReference: CN=DC,CN=Topology,CN=Domain System Volume,CN=DFSR-Glob
 alSettings,CN=System,DC=active,DC=htb

# SYSVOL Subscription, Domain System Volume, DFSR-LocalSettings, DC, Domain Con
 trollers, active.htb
dn: CN=SYSVOL Subscription,CN=Domain System Volume,CN=DFSR-LocalSettings,CN=DC
 ,OU=Domain Controllers,DC=active,DC=htb
objectClass: top
objectClass: msDFSR-Subscription
cn: SYSVOL Subscription
distinguishedName: CN=SYSVOL Subscription,CN=Domain System Volume,CN=DFSR-Loca
 lSettings,CN=DC,OU=Domain Controllers,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718185123.0Z
whenChanged: 20180718185629.0Z
uSNCreated: 12534
uSNChanged: 12720
showInAdvancedViewOnly: TRUE
name: SYSVOL Subscription
objectGUID:: xPhvFhzqdki94xWwLYVEsQ==
objectCategory: CN=ms-DFSR-Subscription,CN=Schema,CN=Configuration,DC=active,D
 C=htb
dSCorePropagationData: 16010101000000.0Z
msDFSR-RootPath: C:\Windows\SYSVOL\domain
msDFSR-StagingPath: C:\Windows\SYSVOL\staging areas\active.htb
msDFSR-Enabled: TRUE
msDFSR-Options: 0
msDFSR-ContentSetGuid:: aPos00Tz8Uy1XJMrqh8w+Q==
msDFSR-ReplicationGroupGuid:: ag0jqthuHEejwTPI5XeWuA==
msDFSR-ReadOnly: FALSE

# BCKUPKEY_7c680e61-140b-4da8-a944-42124c2034a8 Secret, System, active.htb
dn: CN=BCKUPKEY_7c680e61-140b-4da8-a944-42124c2034a8 Secret,CN=System,DC=activ
 e,DC=htb

# BCKUPKEY_P Secret, System, active.htb
dn: CN=BCKUPKEY_P Secret,CN=System,DC=active,DC=htb

# BCKUPKEY_8ed5b591-3663-43d1-bd88-75bc92c52b3c Secret, System, active.htb
dn: CN=BCKUPKEY_8ed5b591-3663-43d1-bd88-75bc92c52b3c Secret,CN=System,DC=activ
 e,DC=htb

# BCKUPKEY_PREFERRED Secret, System, active.htb
dn: CN=BCKUPKEY_PREFERRED Secret,CN=System,DC=active,DC=htb

# SVC_TGS, Users, active.htb
dn: CN=SVC_TGS,CN=Users,DC=active,DC=htb
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: SVC_TGS
distinguishedName: CN=SVC_TGS,CN=Users,DC=active,DC=htb
instanceType: 4
whenCreated: 20180718201438.0Z
whenChanged: 20220429154049.0Z
displayName: SVC_TGS
uSNCreated: 20508
uSNChanged: 94276
name: SVC_TGS
objectGUID:: NTKdjAodsU2Z7j94PRqb1g==
userAccountControl: 66048
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 131766552903202773
pwdLastSet: 131764184784027640
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAArxktGAS1AL49Gv12TwQAAA==
accountExpires: 9223372036854775807
logonCount: 6
sAMAccountName: SVC_TGS
sAMAccountType: 805306368
userPrincipalName: SVC_TGS@active.htb
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=active,DC=htb
dSCorePropagationData: 20180718201438.0Z
dSCorePropagationData: 16010101000000.0Z
lastLogonTimestamp: 132957204496659494

# search reference
ref: ldap://ForestDnsZones.active.htb/DC=ForestDnsZones,DC=active,DC=htb

# search reference
ref: ldap://DomainDnsZones.active.htb/DC=DomainDnsZones,DC=active,DC=htb

# search reference
ref: ldap://active.htb/CN=Configuration,DC=active,DC=htb

# search result
search: 2
result: 0 Success

# numResponses: 225
# numEntries: 221
# numReferences: 3
```
