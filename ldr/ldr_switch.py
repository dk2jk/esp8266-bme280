# ldr.py
''' ldr.1 gegen GND, ldr.2 an 6k8.1, 6k8.2 an 3.3V
ldr.2 an a0
'''
import machine
from Led import Led
from Ldr import Ldr
from time import sleep
adc = machine.ADC(0)
led=Led(2)
ldr=Ldr()

def input_grenzwert(s):
    input(s)
    return adc.read()


ldr.set_hell(input_grenzwert('hellster wert?'))
ldr.set_dunkel(input_grenzwert('Dunkel- wert?'))

while True:
    y=ldr.prozent()
    print ('Helligkeit= ',y,' %')
    if y >55:
        led.an()
    elif y < 45:
        led.aus()
    sleep(.1)
