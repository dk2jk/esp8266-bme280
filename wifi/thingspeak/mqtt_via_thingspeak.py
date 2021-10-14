# mqtt_via_thingspeak
# daten ansehen unter...
# https://thingspeak.com/channels/1533730/widgets/366313
# https://thingspeak.com/channels/1533730

from umqtt.simple import MQTTClient
from timer import Timer
import time
from BME280_1 import *
from machine import I2C,Pin

# bme
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
bme = BME280(address=0x77, i2c=i2c)

# thingspeak
SERVER = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", SERVER)
CHANNEL_ID    = "1533730"
WRITE_API_KEY = 'OFSMOZN1COHG6PAV'
topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
def zeit():
    x= time.gmtime()  #(2021, 10, 12, 15, 50, 55, 1, 285)
    return "Time: {:02d}.{:02d}.{:04d} {:02d}:{:02d}.{:02d}".format( x[2],x[1],x[0], x[3],x[4],x[5])

def send():
    payload ="field1="+str(bme.temperature)+\
            "&field2="+str(bme.humidity)+\
            "&field3="+str(bme.pressure)
    client.connect()
    client.publish(topic, payload)
    client.disconnect()

timer1= Timer(15) # alle 15 sec
while True:
    if timer1.event():
        send()
        x= time.gmtime()               
        print(" Daten an thingspeak gesendet", zeit() )
              