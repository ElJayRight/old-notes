for line in open('input_6','r'):
    pass
line = line.strip()
for i in range(len(line)-13):
    x = line[i:i+14]
    flag = False
    for letter in x:
        if x.count(letter)!=1:
            flag = True
    if flag==False:
        print(i+14)
        exit()