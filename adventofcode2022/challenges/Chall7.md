# Python
```python
counter = 0
for line in open("input_4",'r'):
    x,y = line.strip().split(',')
    x1,x2 = x.split('-')
    y1,y2 = y.split('-')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if (x1 in range(y1,y2+1) and x2 in range(y1,y2+1)) or (y1 in range(x1,x2+1) and y2 in range(x1,x2+1)):
        counter +=1

print(counter) 
```