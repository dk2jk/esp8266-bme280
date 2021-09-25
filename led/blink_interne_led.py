from machine import Pin
from time    import sleep

led= Pin(2,Pin.OUT)

while True:
    sleep(.5)
    led.value(1)
    sleep(.5)
    led.value(0)
    print(i)
