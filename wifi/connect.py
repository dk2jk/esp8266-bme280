import network
from my_wlan import WiFi_SSID, WiFi_PW
from timer import Timer
from time import sleep

TIMEOUT=3 #sec
timeout= Timer(TIMEOUT)
wlan = network.WLAN(network.STA_IF)

def do_connect():   
    wlan.active(True)
    print('verbunden mit :',end=' ')    
    timeout.set(TIMEOUT)
    while wlan.isconnected() == False:
        wlan.connect(WiFi_SSID, WiFi_PW)
        sleep(.33)
        print('.', end = '')
        if timeout.event():
            print('\nnetwork timeout nach {} sekunden'.format(TIMEOUT))
            wlan.disconnect()
            return False
    print( wlan.ifconfig())
    return True

if __name__ =='__main__':
    do_connect()
