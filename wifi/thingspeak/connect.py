import network
from network import WLAN
from time import sleep
try:
    from my_wlan import WiFi_SSID, WiFi_PW
except:
    #my_wlan.py
    WiFi_SSID, WiFi_PW= "meine ssid","mein passwort"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def disconnect():
    wlan.active(False)

def do_connect():
    """mein wlan wird nachts ausgeschaltet
    damit das programm nicht in einer warteschleife haengen bleibt,
    wird hier einiges ueberprueft
    wlan.isconnected() kommt nach max 4 sec
    """
    ok=False
    try:
        nets = wlan.scan()
    except:
        print('*** WLAN scan ohne Antwort')

        ok=False
        return ok
    print(nets)
    for net in nets:
        ssid=net[0].decode()
        if ssid== WiFi_SSID:
            print('SSid "{}" gefunden'.format(WiFi_SSID))
            wlan.connect(ssid,  WiFi_PW)
            n=0
            sleep(1)
            while not  wlan.isconnected():               
                print('.',end='')
                n=n+1
                if n==10:  # 10 sek timeout
                    break
                sleep(1)
            if n==10:
                print("*** falsches passwort ?")  # hilfe bei timeout
            else:
                print('WLAN connection succeeded!')
                print(wlan.ifconfig())
                ok=True
                break
        else:           
            ok=False
    if not ok:
        print('*** keine verbindung zu ssid "{}" moeglich'.format(WiFi_SSID))
    return ok
    
if __name__ =='__main__':
    do_connect()
    disconnect()
    pass

