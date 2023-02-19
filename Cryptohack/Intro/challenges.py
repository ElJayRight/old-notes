def ASCII():
    input = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    print(''.join([chr(x) for x in input]))


def HEX():
    input = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
    print(bytes.fromhex(input))

def B64():
    import base64
    input = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    print(base64.b64encode(bytes.fromhex(input)))
from Crypto.Util.number import *
def BytesandBigInts():
    input = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    print(long_to_bytes(input))

from pwn import xor
def XORStarter():
    input = "label"
    print("crypto{"+str(xor(input,13))+"}")

def XORProperties():
    k1 ='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
    k2k1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
    k2k3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
    fk1k2k3 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
    print(xor(bytes.fromhex(k2k3),bytes.fromhex(k1),bytes.fromhex(fk1k2k3)))

def favouritebyte():
    input = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
    input = bytes.fromhex(input)
    for i in range(1,256):
        r = xor(chr(i),input)
        if b'crypto' in r:
            print(r)

def XORchall():
    input = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    input = bytes.fromhex(input)
    print(xor('myXORkey',input))