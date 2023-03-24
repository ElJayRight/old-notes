x = ''
for line in open('byte.dmp','r'):
    line = line.strip().split(' ')
    for i in line:
        if i!='0':
            x+=chr(int(i))

with open('stage3.ps1','w') as f:
    f.write(x+'\n')
