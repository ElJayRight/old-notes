## Python
```python
score = 0
key = {"X":1,"Y":2,"Z":3,"A":1,"B":2,"C":3}
for line in open("input_2",'r'):
    x,y = [key[x] for x in line.strip().split()]
    score+=y
    if x==y:
        score+=3
    elif x%3+1==y:
        score+=6
print(score)
```