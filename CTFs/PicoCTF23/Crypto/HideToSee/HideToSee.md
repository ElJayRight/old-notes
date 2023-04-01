Extract from the img with steghide.
```bash
steghide extract -sf atbash.jpg
```

This gives a encrypted.txt file. Run it through an atbash cipher and it prints the flag.
```python
def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - ord(char) + ord('A'))
            else:
                result += chr(ord('z') - ord(char) + ord('a'))
        else:
            result += char
    return result
print(atbash_cipher('krxlXGU{zgyzhs_xizxp_7142uwv9}'))
```

Flag:
```
picoCTF{atbash_crack_7142fde9}
```