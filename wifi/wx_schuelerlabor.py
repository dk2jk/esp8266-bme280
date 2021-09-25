import uos
uname = uos.uname()
from read_bme import read_bme
from led import led
from time import sleep


try:
    ap.active()
except:
    from start_access_point import *
    print("Connect to " + ssid + ":" + "password = " + password);
    print("Visit: " + ap.ifconfig()[2] + ":80")

print('===== ===== =====')

titel= "WX Sch&uumllerlaber"
res_01 = """<html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="10">
    </head>
    <body>
    <h1>{}</h1>""".format(titel)
def send_bme(x):
    res_02= """
    </body> Messergebnisse: <br>
    {}
    </html>""".format(x) 
    return res_02

def led_blitz():
    led.on()
    sleep(.2)
    led.off()
    
res_machine = "Gegenstelle: " + uname.machine + "<br/>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    youraddr = "Eigene Adresse: "+ str(addr)
    request = conn.recv(1024)

    conn.send(res_01)
    conn.send(res_machine)
    ##conn.send("<br/><br/>")
    conn.send(youraddr)
    print(youraddr)
    conn.send("<br/><br/>")
    #conn.send(request)
    x= read_bme()
    y= send_bme(x)
    print(x)
    conn.send(y)
    conn.close()
    led_blitz()
    print()