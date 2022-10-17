# Overview
For each packet you will be able to see the packet number, time, source, destination, protocol, length and packet info.
Wireshark will also colour code things in order of danger.

# Collection methods

## Network taps
A physcial implant that can be placed on the wire. LAN stars are a common example.

## MAC floods
Stressing the switch to fill up the CAM table. Which when flooded will no longer give out mac addresses. Resulting in the packets being sent from all ports of the switch.

## ARP Posioning
Redirect the traffic from the host to the machine monitoring from.

# Filtering Captures
## Logic operators
Just like C++

## Basic Filtering
filter by ip
```wireshark
ip.addr == <IP Address>
```

can also filter by source and destination
```wireshark
ip.src == <SRC IP Address> and ip.dst == <DST IP Adress>
```

Filter by port
TCP
```wireshark
tcp.port eq <Port #> or <Protocol Name>
```
UDP
```wireshark
udp.port eq <Port #> or <Protocol Name>
```

# Packet Dissection
OSI more like **NOSI**
## Packet Details
Shows the 7 layers.
Frame, source (MAC), source (IP), Protocol, Application Protocol, Application Data

# ARP Traffic
If you filter for arp and then check the reply of each packet.

# ICMP Traffic
Looking at the type can tell you what packet was send, 8 for request and 0 for reply.
You can also see the data and time.

# TCP Traffic
Lets you see which tcp flags are passed in each packet. Can also detect nmap scans

# DNS Traffic
The query field of the packet contains both the query and the ID of the packet.

# HTTP Traffic
the protocol hierarchy and endpoint features of the statistics tab are very useful.