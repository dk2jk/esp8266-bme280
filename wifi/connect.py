import network
from my_wlan import WiFi_SSID, WiFi_PW

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WiFi_SSID, WiFi_PW)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

if __name__ =='__main__':
    do_connect()
