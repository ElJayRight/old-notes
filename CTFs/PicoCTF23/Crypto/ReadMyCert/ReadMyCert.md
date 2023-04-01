Cat the file get the b64 decode it the run strings and grep for picoCTF
```bash
cat readmycert.csr | awk -F'-' '{print $1}'|base64 -d|strings|grep pico
```

Flag:
```
picoCTF{read_mycert_41d1c74c}
```