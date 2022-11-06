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