try:
  import usocket as socket
except:
  import socket

import network
import time

import esp
esp.osdebug(None)

import gc
gc.collect()

from config import *

ap = network.WLAN(network.AP_IF)
ap.active(False)
time.sleep(2)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

ap.ifconfig(('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
print('Wlan Accesspoint running')
print(ap.ifconfig())


