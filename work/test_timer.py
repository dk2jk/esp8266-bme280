# test hardware timer

from machine import Timer
import micropython
micropython.alloc_emergency_exception_buf(100)

class Timeout:
    def __init__(self):
        self.timeout=False
        self.t1= Timer(-1)
    def start(self,ms):
        self.t1.init(mode=Timer.ONE_SHOT, period=ms, callback=self.timeout_funktion)        
    def timeout_funktion(self,t):
        self.timeout=True

