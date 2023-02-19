# Hi
I got a pico w and it has wifi! I wonder if i could do a deauth attack on it? This could work cause it does have a wifi chip and if i can find some sort of python library or something that can put the chip into monitor mode it should 'just work'.

This isn't a thing :(. From what I can find no one has tried this. It is possible tho cause the card can be put into monitor mode. [link](https://github.com/adafruit/circuitpython/pull/5537)

# Reversing a library
It imports this wifi library so I should just be able to view the python `__init__.py` file and see what the library can do.

Turns out its not a py file. There is a monitor.c file though.

This file is awesome cause there is the attached python code that the c code shall compile(?) into.
`shared-bindings/wifi/`
```python
class Monitor:

"""For monitoring WiFi packets."""
def __init__(self, channel: Optional[int] = 1, queue: Optional[int] = 128) -> None:
"""Initialize `wifi.Monitor` singleton.

:param int channel: The WiFi channel to scan.

:param int queue: The queue size for buffering the packet.
"""
...
channel: int
"""The WiFi channel to scan."""
queue: int
"""The queue size for buffering the packet."""
def deinit(self) -> None:
"""De-initialize `wifi.Monitor` singleton."""
...
def lost(self) -> int:
"""Returns the packet loss count. The counter resets after each poll."""
...
def queued(self) -> int:
"""Returns the packet queued count."""
...
def packet(self) -> dict:
"""Returns the monitor packet."""
...
```
Semi python code.

So you can scan wifi channels and return a pre made packet. All that is left to figure out if you can send your own packets.

# Documentation
I found the documentation (which is a lot better then reading source code) [link](https://docs.circuitpython.org/en/latest/shared-bindings/wifi/index.html)

There is a `wifi.packet` class that allows you to create your own packets.

## How do packets work?
The documentation has 8 line about the `wifi.packet` class. Mainly saying that the parameters are objects.

The class is a enum class.
```c
#include "py/enum.h"
typedef enum {
    PACKET_CH,
    PACKET_LEN,
    PACKET_RAW,
    PACKET_RSSI,
} wifi_packet_t;
```

This isn't really helpful :|

Lets just see what happens
