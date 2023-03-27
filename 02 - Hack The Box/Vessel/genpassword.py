from PySide2.QtCore import *
length = 32
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={}[]|:;<>,.?'
for i in range(0,999):
    qsrand(i)
    password = ''
    for i in range(length):
        idx = qrand() % len(charset)
        nchar = charset[idx]
        password += str(nchar)
    print(password)