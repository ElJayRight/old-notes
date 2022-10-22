# Contents
- Task Description
- Notes
- Solve Script

## Task Description
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?

## Notes
wget the file and run strings on it.
The output has alot of b64, first thought was to run a grep for pico as an easy win which works.

flag is:
```flag
picoCTF{5tRIng5_1T_d66c7bb7}
```

## Solve Script
```bash
stings strings | grep pico
```


---
Creation date: 09-10-2022

Last modified date: Sunday 9th October 2022
***

