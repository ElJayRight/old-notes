i = '72696854 646e4164 616e6946 2121216c'
i = i.split()
out = ''
for j in i:
	v = []
	for x in range(len(j)//2):
		v.append(chr(int(j[x*2:(x*2)+2],16)))
	out+= ''.join(v[::-1])
print(out)