IP: 10.129.144.176

Nmap Scan
```bash
nmap -sC -sV 10.129.144.176
Starting Nmap 7.80 ( https://nmap.org ) at 2022-03-08 17:56 AEDT
Nmap scan report for 10.129.144.176
Host is up (0.23s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
P: 10.129.144.176
```
Task 1.
- What does the acronym VM stand for? 
	 - Virtual Machine 

Task 2.
- What tool do we use to interact with the operating system in order to start our VPN connection? 
	- Terminal

Task 3.
What service do we use to form our VPN connection? 
	openvpn

Task 4.
What is the abreviated name for a tunnel interface in the output of your VPN boot-up sequence output? 
	tun

Task 5.
What tool do we use to test our connection to the target? 
	ping

Task 6.
What is the name of the tool we use to scan the target's ports? 
	nmap

Task 7.
What service do we identify on port 23/tcp during our scans? 
	telnet

Task 8.
What username ultimately works with the remote management login prompt for the target? 
	root

Task 9.
Submit root flag:
login to the telnet server
```bash
telnet <ip>
```
enter root as username and then cat out flag.txt
```bash
b40abdfe23665f766f9c61ecba8a4c19
```