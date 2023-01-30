counter = 0
sum = 0
array = []
for line in open("input_3",'r'):
    if counter==3:
        i = [x for x in array[0] if x in array[1] and x in array[2]][0]
        if i in i.lower():
            sum += ord(i)-96
        else:
            sum += ord(i)-38
        counter=0
        array=[]
    array.append(list(line.strip()))
    counter+=1
i = [x for x in array[0] if x in array[1] and x in array[2]][0]
if i in i.lower():
    sum += ord(i)-96
else:
    sum += ord(i)-38
print(sum)