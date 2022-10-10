Links [[00 - Global Index (Start Here!)]] [[01 - PicoGym]] [[Forensics]]

# [[01 - Information]]
### Contents
***
- [Task Description](01%20-%20Information.md#Task%20Description)
- [Notes](01%20-%20Information.md#Notes)
- [Solve Script](01%20-%20Information.md#Solve%20Script)


### Task Description
---
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg)

### Notes
---
Its an image so exiftool to start.
There is a b64 blob which happens to be the flag :)
```flag
picoCTF{the_m3tadata_1s_modified}
```

### Solve Script
---
```bash
exiftool cat.jpg | grep License | awk -F": " '{print $2}' | base64 -d
```


---
Creation date: 10-10-2022
Last modified date: Monday 10th October 2022
***
