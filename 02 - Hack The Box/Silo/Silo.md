# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/silo 10.10.10.82

PORT      STATE SERVICE      VERSION
80/tcp    open  http         Microsoft IIS httpd 8.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/8.5
|_http-title: IIS Windows Server
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
1521/tcp  open  oracle-tns   Oracle TNS listener 11.2.0.2.0 (unauthorized)
8080/tcp  open  http         Oracle XML DB Enterprise Edition httpd
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=XDB
|_http-server-header: Oracle XML DB/Oracle Database
|_http-title: 401 Unauthorized
49159/tcp open  oracle-tns   Oracle TNS listener (requires service name)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   302: 
|_    Message signing enabled but not required
|_clock-skew: mean: -26s, deviation: 0s, median: -26s
| smb2-time: 
|   date: 2023-05-14T14:43:43
|_  start_date: 2023-05-14T14:40:51
| smb-security-mode: 
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: supported

```