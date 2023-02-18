from Crypto.Cipher import AES
import lookup
def xor(data,key):
    r = b''
    for i in range(len(data)):
        r+= bytes([data[i] ^ key[i%len(key)]])
    return r
aes_key = bytes.fromhex('f2003c143dc8436f39ad6f8fc4c24f3d35a35d862e10b4c654aedc0ed9dd3ac5')
f = open('thepackets.raw','rb')
while True:
    xor_key = f.read(4)
    session_key = xor(f.read(16),xor_key)
    enc_flag = xor(f.read(4),xor_key)
    packet_len = xor(f.read(4),xor_key)
    packet_type = xor(f.read(4),xor_key)
    packet_len_int = int.from_bytes(packet_len,'big')
    if int.from_bytes(enc_flag,'big') ==0:
        tlv = xor(f.read(packet_len_int-8),xor_key)
    else:
        aes_iv = xor(f.read(16),xor_key)
        cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
        tlv = xor(f.read(packet_len_int-24),xor_key)
        tlv = cipher.decrypt(tlv)
    while len(tlv) > 0:
        tlv_len = tlv[:4]
        tlv_type = tlv[4:8]
        tlv_type_1 = tlv_type[0:2]
        tlv_type_2 = int.from_bytes(tlv_type[2:4],'big')
        tlv_len_int = int.from_bytes(tlv_len,'big')
        tlv_value = tlv[8:tlv_len_int]
        try:
            print(f"Session Key: {session_key}\tpacket length: {packet_len_int}\tTLV: {lookup.MSFType(tlv_type_2).name}")
            if lookup.MSFType(tlv_type_2).name == "TLV_TYPE_CHANNEL_DATA":
                f2 = open("file.zip",'ab')
                f2.write(tlv_value)
                f2.close()
        except:
            print(f"Unknown TLV type: {tlv_type_2}")
        
        tlv = tlv[tlv_len_int:]
f.close()
