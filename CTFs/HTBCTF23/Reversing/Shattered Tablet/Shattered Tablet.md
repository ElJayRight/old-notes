Opening the file in Ghidra shows this if block:
```c
  printf("Hmmmm... I think the tablet says: ");
  fgets((char *)&local_48,0x40,stdin);
  if (((((((((local_30._7_1_ == 'p') && (local_48._1_1_ == 'T')) && (local_48._7_1_ == 'k')) &&
          ((local_28._4_1_ == 'd' && (local_40._3_1_ == '4')))) &&
         ((local_38._4_1_ == 'e' && ((local_40._2_1_ == '_' && ((char)local_48 == 'H')))))) &&
        (local_28._2_1_ == 'r')) &&
       ((((local_28._3_1_ == '3' && (local_30._1_1_ == '_')) && (local_48._2_1_ == 'B')) &&
        (((local_30._5_1_ == 'r' && (local_48._3_1_ == '{')) &&
         ((local_30._2_1_ == 'b' && ((local_48._5_1_ == 'r' && (local_40._5_1_ == '4')))))))))) &&
      (((local_30._6_1_ == '3' &&
        (((local_38._3_1_ == 'v' && (local_40._4_1_ == 'p')) && (local_28._1_1_ == '1')))) &&
       (((local_30._3_1_ == '3' && (local_38._1_1_ == 'n')) &&
        (((local_48._4_1_ == 'b' && (((char)local_28 == '4' && (local_40._1_1_ == 'n')))) &&
         ((char)local_38 == ',')))))))) &&
     ((((((((char)local_40 == '3' && (local_48._6_1_ == '0')) && (local_38._7_1_ == 't')) &&
         ((local_40._7_1_ == 't' && ((char)local_30 == '0')))) &&
        ((local_40._6_1_ == 'r' && ((local_28._5_1_ == '}' && (local_38._5_1_ == 'r')))))) &&
       (local_38._6_1_ == '_')) && ((local_38._2_1_ == '3' && (local_30._4_1_ == '_')))))) {
    puts("Yes! That\'s right!");
  }
```

Carving out the variables using find and replace leaves this:
```
local_30[7]='p'
local_48[1]='T'
local_48[7]='k'
local_28[4]='d'
local_40[3]='4'
local_38[4]='e'
local_40[2]='_'
local_48[0]='H'
local_28[2]='r'
local_28[3]='3'
local_30[1]='_'
local_48[2]='B'
local_30[5]='r'
local_48[3]='{'
local_30[2]='b'
local_48[5]='r'
local_40[5]='4'
local_30[6]='3'
local_38[3]='v'
local_40[4]='p'
local_28[1]='1'
local_30[3]='3'
local_38[1]='n'
local_48[4]='b'
local_28[0]='4'
local_40[1]='n'
local_38[0]=','
local_40[0]='3'
local_48[6]='0'
local_38[7]='t'
local_40[7]='t'
local_30[0]='0'
local_40[6]='r'
local_28[5]='}'
local_38[5]='r'
local_38[6]='_'
local_38[2]='3'
local_30[4]='_'
```

Then print the flag:
```python
flag = []
for i in [local_48,local_40,local_38,local_30,local_28]:
	flag.extend(i)
r = ''.join(flag)
print(r)
```

Flag:
```
HTB{br0k3n_4p4rt,n3ver_t0_b3_r3p41r3d}
```