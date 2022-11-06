IP: 10.129.1.14
Nmap Scan
```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2022-03-08 18:13 AEDT
Nmap scan report for 10.129.1.14
Host is up (0.22s latency).
Not shown: 990 closed ports
PORT      STATE    SERVICE  VERSION
21/tcp    open     ftp      vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.30
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
```

Task 1.
	- What does the 3-letter acronym FTP stand for? 
		- File Transfer protocol

Task 2.
	- What communication model does FTP use, architecturally speaking? 
		- client-server model

Task 3.
	- What is the name of one popular GUI FTP program? 
		-Filezilla

Task 4.
	- Which port is the FTP service active on usually? 
		- 21 TCP

Task 5.
	- What acronym is used for the secure version of FTP? 
		- SFTP (like https is for http)

Task 6.
	- What is the command we can use to test our connection to the target? 
		- ping

Task 7.
	- From your scans, what version is FTP running on the target? 
		- vsftpd 3.0.3

Task 8.
	- From your scans, what OS type is running on the target? 
		- Unix

Task 9.
	- Submit root flag:
		- Login in to ftp server as anonymous
		```bash
		ftp <ip> -u anonymous
		```
		Give anything for a password
		- You can not cat from the ftp server but instead need to download the file. (using get)
		```
		035db21c881520061c53e0536e44f815
		```