## Python
```python
array = []
counter =0
for line in open("input_1",'r'):
    if line.strip() =="":
        array.append(counter)
        counter=0
    else:
        counter+=int(line.strip())
array.append(counter)
array.sort()
print(sum(array[-3:]))
```