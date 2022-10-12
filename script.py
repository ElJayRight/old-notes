import os
list = os.listdir()
list.remove("script.py")
print(os.getcwd())
list.sort()
dict = {"/":[]}
v = os.getcwd()
'''
for i in list:
    if i.startswith('.')==0:
        if i.endswith('.md'):
            dict["/"].append(i)
        else: 
            dict[i]=dict
    '''        
def get_dir(list,v):
    dict = {v:[]}
    indent = v.replace('/home/kali/Notes/','').count('/')
    #print(' '*indent+v.replace('/home/kali/Notes/',''))
    for i in sorted(list):
        if i.startswith('.')==0:
            if i.endswith('.md') or i.endswith('.sh') or i.endswith('.jpg') or i.endswith('.py') or i.endswith('.txt') or i.endswith('.bin') or '.' in i:
                if i.endswith('.md'):
                    indent = v.count('/')-3
                    if v.split('/')[-1]==i.replace('.md',''):
                        indent-=1
                    print('  '*indent+"* ["+i.replace('.md','')+"]("+v.replace('/home/kali/Notes/','').replace(" ","%20")+'/'+i.replace(" ","%20")+")")
            else:
                v +="/"+i
                dict[i]=get_dir(os.listdir(v),v)
                v = v.replace("/"+i,"")
    return dict
out = get_dir(list,v)