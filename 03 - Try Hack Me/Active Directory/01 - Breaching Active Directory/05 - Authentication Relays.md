Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Breaching Active Directory]]

# [05 - Authentication Relays]
## Notes
---
Server Message Block (SMB)
Allows communication between clients (like workstations) and a server
Exploits for NetNTLM auth with SMB

- Since the NTLM Challenges can be intercepted, they can be cracked offline to get the password. This is slower then just cracking the NTLM hashes directly.
- Use rogue devices to stage a man in the middle attack, relaying the SMB auth between the cleint and server, which will provide us with an active authenticated session ans access to the target server.

LLMNR, NBT-NS and WPAD
Responder is used to intercept the NetNTLM challenge.
Responder allows a man in the middle attakc by poisoning the responses during NetNTLM auth, tricking the client into talking to you instead of the actual server. On a real LAN it will attempt to poison any LLMNR, NBT-NS and WPAD request.
It can also capture HTTP and SQL requests.

To run responder:
```bash
sudo ./Responder.py -I tun0
```
To crack the hash
```bash
hashcat -m 5600 hash.txt password.txt
```
SVCFILECOPY:FPassword1!