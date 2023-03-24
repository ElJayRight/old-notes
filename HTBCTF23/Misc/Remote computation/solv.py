from pwn import *

def Reply(text):
    try:
        r = round(eval(text),2)
        #print(r)
        if -1337.00 <=r<=1337.00:
            r = str(r).encode()
        else:
            r = b"MEM_ERR"
    except ZeroDivisionError as e:
        r = b"DIV0_ERR"
    except SyntaxError as e:
        r = b"SYNTAX_ERR"
    return r

p = remote('138.68.162.218',30030)
#print(p.recv())
p.sendline(b'1')
for i in range(500):
    reply = p.recv()
    #print(reply)
    r = reply.split(b":")[1].split(b"=")[0]
    o = Reply(r)
    #print(o)
    p.sendline(o)
print(p.recvall())