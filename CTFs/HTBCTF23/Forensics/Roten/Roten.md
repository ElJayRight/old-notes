Given a pcap file.

# Solution
Reading the challenge description there is mention of an uploaded shell. So similar to Plain Tleasure we can look for a form.

There are 3 in the pcap file but one stands outas being 7kb. Downloading and then opening this shows a php shell.

Removing the form padding and changing the eval to be a print we can safely execute the php code.

This gives a second stage which contains the flag.
```
cat stage2.html | grep flag
HTB{W0w_ROt_A_DaY}
```