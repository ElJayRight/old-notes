# Rant
My ad blocker stopped working and now I have to deal with watching 2 30sec videos before i can waste time watching youtube. FOR EACH VIDEO! This is bad. So im going to do some DNS filtering thing? and remove them from the dns server, which I also have to set up. idk how to do most of that but there is something called Ad guard which is supported on Raspberry Pi's so time to figure out how this all works.

# DNS
Domain name service or system doesnt matter, this is what causes ads and trackers. My current DNS server is my router. So that needs to be changed. *somehow*. turns out adguard can do this too.
# The install bit
```bash
curl -s -S -L https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v
```
Auto install and set up. Going to the GUI and spamming next.

Then changing all my dns servers on devices individually, and voila no more ads.

Fin.
