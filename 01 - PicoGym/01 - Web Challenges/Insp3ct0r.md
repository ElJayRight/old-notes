# Contents
- Task Description
- Notes
- Sovle Script

## Task Description
Kishor Balan tipped us off that the following code may need inspection: `https://jupiter.challenges.picoctf.org/problem/44924/`

## Notes
Looking at the html of the page shows the first part of the flag. There is also reference to custom css and js pages.
Checking the network tab of dev tools in chrome gives both links.
```bash
https://jupiter.challenges.picoctf.org/problem/44924/mycss.css
https://jupiter.challenges.picoctf.org/problem/44924/myjs.js
```
Adding the flags together gives:
```flag
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}
```

## Sovle Script
```python
import requests

r1 = requests.get("https://jupiter.challenges.picoctf.org/problem/44924/")
a = r1.content.decode().split("flag: ")[1].split(' ')[0]
  
r2 = requests.get("https://jupiter.challenges.picoctf.org/problem/44924/mycss.css")
b = r2.content.decode().split("flag: ")[1].split(' ')[0]

r3 = requests.get("https://jupiter.challenges.picoctf.org/problem/44924/myjs.js")
c = r3.content.decode().split("flag: ")[1].split(' ')[0]

print(a+b+c)
```


---
Creation date: 08-10-2022

Last modified date: Sunday 8th October 2022
***
