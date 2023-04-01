So we cant use normal linux commands.

What about there relative path?
```
../../../bin/ls ../../
```

Yep this works.

Used this to cat the box config file.
```
../../bin/cat ../../challenge/config-box.py
```

Which has the path for the flag.
```
with open("/home/ctf-player/blargh/flag.txt", "w") as f:
```

Flag:
```
picoCTF{5p311ch3ck_15_7h3_w0r57_6a2763f6}
```