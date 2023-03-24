dict = {}
with open('window.bat','r') as f:
    for line in f:
        if line[0] =="%" and line[5] == '%':
            line = line[7:-2]
            name = line[:10]
            value = line[11:]
            dict[name] = value
        else:
            obfs = line.split("%")
            out = ''
            for i in obfs:
                if len(i) ==10 and '@' not in i:
                    out+=dict[i]
            print(out)