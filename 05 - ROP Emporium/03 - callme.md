Links [[00 - Global Index (Start Here!)]] [[ROP Emporium]]

# [[callme]]
### Contents
***
- [Task Description](03%20-%20callme.md#Task%20Description)
- [32 bit](03%20-%20callme.md#32%20bit)

### Task Description
***
Reliably make consecutive calls to imported functions.  
Use some new techniques and learn about the Procedure Linkage Table.

### 32 bit
***
Reading the site we need to call three functions while passing in the same three arguments.

args:  `0xdeadbeef`, `0xcafebabe`, `0xd00df00d`
functions: callme_one(), callme_two(), callme_three()

Getting the memory locations of the three functions:
callme_one():     `0xf7fc0d3d`
callme_two():     `0xf7fc0755`
callme_three():   `0xf7fc0855`

We also need a a way to remove the arguments off the stack after before we add the next function or they wont populate correctly.
You can find this gadget by running ropper:
```bash
ropper -f callme32 --search pop

0x080487f9: pop esi; pop edi; pop ebp; ret; 
```
Using this memory location the exploit chain will look like this:

Offset
callme1
gadget
arg1
arg2
arg3
callme2
gadget
arg1
arg2
arg3
callme3
gadget
arg1
arg2
arg3

Next is to find the buffer size.
44

encode everything in little endian and send it to a payload.
