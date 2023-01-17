header = 0
data = [[],[],[],[],[],[],[],[],[]]
for line in open('input_5','r'):
    if line.strip() =='':
        header =-1
        for i in range(len(data)):
            data[i] = ''.join(data[i][:-1][::-1]).replace(' ','')
    if header==0:
        d = line.strip().replace(']',' ').replace('[',' ')[1:]
        for i in range(0,33,4):
            try:
                data[i//4].append(d[i])
            except:
                data[i//4].append('')
    elif header ==1:
        a,f,t = line.strip().split(' ')[1::2]
        data[int(t)-1]+=data[int(f)-1][int(a)*-1:]
        data[int(f)-1] = data[int(f)-1][:-int(a)]
    else:
        header =1
for i in data:
    print(i[-1],end='')