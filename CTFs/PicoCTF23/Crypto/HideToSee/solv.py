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
