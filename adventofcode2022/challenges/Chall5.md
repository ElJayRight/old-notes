# Python
```python
sum = 0
for line in open("input_3",'r'):
    line=line.strip()
    length = len(line)
    x = list(line[:length//2])
    y = list(line[length//2:])
    i = [z for z in x if z in y][0]
    if i in i.lower():
        sum += ord(i)-96
    else:
        sum += ord(i)-38
print(sum)
```