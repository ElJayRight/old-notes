Looking at strings there are two passwords:
```
PasswordNumeroUno
0wTdr0wss4P -> P4ssw0rdTw0
```

Third flag:

In ghidra there is a xor with local_38 which will be the value of the third flag.

Setting a break point before the xor function will have the pointer (location in hex) of the string that will store the password. After this set another breakpoint after the xor call and read out the third flag.

In GDB
```
> b *0x401369
> run
> i r
rax 0x7fffffffde00
> s
> x/4 0x7fffffffde00
0x72696854	0x646e4164	0x616e6946	0x2121216c
```

Which will be the flag. Decoder
```python
i = '72696854 646e4164 616e6946 2121216c'
i = i.split()
out = ''
for j in i:
	v = []
	for x in range(len(j)//2):
		v.append(chr(int(j[x*2:(x*2)+2],16)))
	out+= ''.join(v[::-1])
print(out) #ThirdAndFinal!!!
```

With all this answering the questions from the nc channel gives this flag:
```
HTB{l1c3ns3_4cquir3d-hunt1ng_t1m3!}
```
