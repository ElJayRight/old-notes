IP: 10.129.96.194

Nmap Scan
```bash
nmap -sC -sV 10.129.96.194
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: EXPLOSION
|   NetBIOS_Domain_Name: EXPLOSION
|   NetBIOS_Computer_Name: EXPLOSION
|   DNS_Domain_Name: Explosion
|   DNS_Computer_Name: Explosion
|   Product_Version: 10.0.17763
|_  System_Time: 2022-04-16T16:17:28+00:00
| ssl-cert: Subject: commonName=Explosion
| Not valid before: 2022-04-15T16:14:51
|_Not valid after:  2022-10-15T16:14:51
|_ssl-date: 2022-04-16T16:17:37+00:00; 0s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-04-16T16:17:29
|_  start_date: N/A

```

Task 1.

- What does the 3-letter acronym RDP stand for? 
	- Remote desktop protocol


Task 2.

- What is a 3-letter acronym that refers to interaction with the host through a command line interface? 
	- cli


Task 3.

- What about graphical user interface interactions? 
	- gui


Task 4.

- What is the name of an old remote access tool that came without encryption by default?
	- telnet


Task 5.

- What is the concept used to verify the identity of the remote host with SSH connections? 
	- public-key cryptography


Task 6.

- What is the name of the tool that we can use to initiate a desktop projection to our host using the terminal?
	- xfreerdp


Task 7.

- What is the name of the service running on port 3389 TCP?
	- ms-wbt-server


Task 8.

- What is the switch used to specify the target host's IP address when using xfreerdp?
	- /v:


Task 9.

- Submit the root flag:

	- Login via xfreerdp with the Administrator account
	```bash
	xfreerdp /v:10.129.96.194 /cert:ignore /u:Administrator
	```
	- open flag.txt
	```
	951fa96d7830c451b536be5a6be008a0
	```