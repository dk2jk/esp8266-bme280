import time

class Timer():
    """Verwendung:
meinTimer=Timer( seconds) : Start Timer
meinTimer.event()         : True wenn timer abgelaufen (boolean)
meinTimer.set(seconds)    : set interval,  Timer wird neu gestartet
    """
    
        
    def set( self,sec):
        self.interval = sec
        self.next= time.time()+ self.interval
        
    def __init__(self, sec):
        self.set(sec)
        
    def event( self ):
        t= time.time()
        x= t > self.next
        if x:
            self.next= t + self.interval
            return True
        else:
            return False
        
    def hilfe(self):
        print( self.__doc__)

if __name__ == "__main__":
     t1=Timer(1)
     n=0
     while True:
         if t1.event():
             print (n)
             n+=1
      
        
        
        
    