#Led.py
# led an D5 Port D5= GPIO14 über 220 Ohm gegen GND geschaltet
from machine import Pin
from time import sleep

class Led:
    def __init__(self,pin=14,value=0):
        print(" LED = GPIO{}".format(pin))
        self.led= Pin(pin,Pin.OUT,value=value)
        self.ist_aus=True
    def __call__(self, x): # class ist callable ( wie eine funktion)
        if x:
            self.an()
        else:
            self.aus()
    def an(self):
        self.led(1)  # auch Pin ist callable
        self.ist_aus=False
    def aus(self):
        self.led(0)
        self.ist_aus=True
    def toggle(self):
        if self.ist_aus:
            self(1)   # class ist callable ( wie eine funktion)
        else:
            self(0)

if __name__ =='__main__':
    led1=Led(2)  # 2 = eingebaute led
    while True:
        sleep(.1)
        led1.toggle()
