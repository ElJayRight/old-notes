# SMB
## Outline
Server message block protocol - is a client-server communication used to share file.
It uses a response-request protocol.
Clients connet via TCP/IP (NetBIOS over TCP/IP)

## Enumerating
Enum4Linux
```bash
enum4linux -a 10.10.189.82
```
This can all be done by using nmap and then smbclient

```bash
nmap -sC -sV -p 22,445,139
```
then
```
smbclient -L //10.10.189.82/ -U ''
```
## Exploiting
Log into smb and get the ssh key and the txt file.
chmod 600 for ssh keys

# Telnet
## Outline
Telnet is an application protocol, which lets you execute commands on a remote computer
telnet sent everything in plain text and has been replaced via ssh.
## Enumerating
run a full port scan as top 1000 are closed.
open port on 8012 which is someone's backdoor.

## Exploiting
Run a reverse shell in the backdoor which gives a shell on the box.

# FTP
## Outline
File tranfer protocol.
client-server model.
active and passive FTP
## Enumerating
log in and start downloading shit

## Exploting
Bruteforce with hydra against the mike username
ftp back in and get the flag.


# NFS
Network file system
It mounts a directory
## Enumeration
enumerate shares using showmount.
Then mount the share
```bash
sudo mount -t nfs 10.10.78.73:home /tmp/mount/ -nolock
```

There is a ssh key, log into the box.
## Exploitation
Drop bash with root permissions onto the share and then set the SUID bit.