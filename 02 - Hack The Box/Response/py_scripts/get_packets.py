from scapy.all import *
tcp_stream = b''
def handle_packet(packet):
    global tcp_stream
    if TCP in packet:
        if packet[TCP].sport == 4444 or packet[TCP].dport ==4444:
            tcp_stream +=bytes(packet[TCP].payload)

sniff(offline='dump.pcap',prn=handle_packet)
f = open('thepackets.raw','wb')
f.write(tcp_stream)
f.close()