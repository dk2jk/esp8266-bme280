# reset via gpio16

from machine import Pin

hard_reset= Pin(16,Pin.OUT)

hard_reset(0)
