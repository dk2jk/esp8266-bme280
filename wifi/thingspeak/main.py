from machine import reset_cause
from mqtt_via_thingspeak import *
from connect import do_connect
from deep_sleep import *

x=reset_cause()
y='unbekannt'
if x==6:
    y="hardware"
elif x==5:
    y="deepsleep_reset"
elif x==0:
    y="poweron"
elif x==4:
    y="soft"
elif x==1:
    y= "watchdog"
print("\nreset from '{}'".format(y))


mit_wlan_verbunden=do_connect()
if mit_wlan_verbunden:      
    send()  #mqtt_via_thingspeak
else:
    #disconnect()
    pass
   
blink()
zehn_minuten=60000*10
deep_sleep_ms(zehn_minuten)



