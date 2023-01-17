# Python
```python
'''
Logic
Rock = 1
Paper = 2
Scissors = 3

Lose = 0
draw = 3
Win = 6

Rock beats Scissors
Scissors beats Paper
Paper beats Rock

A = X = Rock
B = Y = Paper
C = Z = Scissors
'''

score = 0
key = {"X":0,"Y":3,"Z":6}
key2 = {"X":2,"Y":0,"Z":1,"A":1,"B":2,"C":3}
for line in open("input_2",'r'):
    x,y = line.strip().split()
    score+=key[y]
    v = (key2[x]+key2[y])%3
    if v==0:
        v=3
    score+=v 
print(score)
```