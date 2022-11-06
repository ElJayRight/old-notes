Task 1.
- What does the 3-letter acronym SMB stand for? 
	- Server message block

Task 2.
- What port does SMB use to operate at? 
	- 445

Task 3.
- What network communication model does SMB use, architecturally speaking? 
	- client-server model

Task 4.
- What is the service name for port 445 that came up in our nmap scan? 
	- microsoft-ds

Task 5.
- What is the tool we use to connect to SMB shares from our Linux distribution? 
	- smbclient

Task 6.
- What is the `flag` or `switch` we can use with the SMB tool to `list` the contents of the share? 
	- -L

Task 7.
- What is the name of the share we are able to access in the end? 
	- workshares


Task 8.
- What is the command we can use within the SMB shell to download the files we find? 
	- get


Task 9.
- Submit the root flag:
	- Go into the WorkShares share
	```bash
	smbclient \\\\<ip>\\<share>
	```
	- then get the flag in James.P folder
	cat it out: 
	```
	5f61c10dffbc77a704d76016a22f1664
	``` 