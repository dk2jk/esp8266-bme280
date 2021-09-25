# ldr.py

import machine

# LDR=  '(L)ight (D)ependent (R)esistor'
class Ldr:
    ''' Verdrahtung als Spannungsteiler:
    ldr.1 gegen GND,
    ldr.2 an 6k8.1,
    6k8.2 an 3.3V
    ldr.2 an a0
    
    intern auf dem Board 'd1 mini':
    a0 an 200k.1
    200k.1 an an0 (CPU) , max 3.3V
    220k.2 an GND
    '''
    def __init__(self):
        # adc object
        self.adc= machine.ADC(0)
        ''' begrenzungswerte ausprobieren mit
        Ldr.read(9 bei 100% und beo 0 % helligkeit
        hier eintragen:
        '''        
        self.set_hell(20)
        self.set_dunkel(800)
        
    def set_hell(self,x):
        self.hell   =x
    def set_dunkel(self,x):
        self.dunkel  =x        
    def _constrain(self, wert):
        ''' wert wir auf hell und dunkel begrenzt'''
        if (wert <= self.hell):
            return self.hell
        if (wert>= self.dunkel):
            return self.dunkel
        return wert
    def read(self):
        ''' adc rohwert 0...1023'''
        return self.adc.read()
    def prozent(self):
        ''' Helligkeit in Prozent'''
        adc_wert= self.read()
        begrenzter_wert=self._constrain(adc_wert) 
        y= 100- 100*(begrenzter_wert-self.hell)/(self.dunkel-self.hell)
        # auf eine stelle hinter dem komma begrenzen
        return round(y,1)
    
if __name__ == '__main__':
    ldr=Ldr()
    print ('  Adc_wert= ',ldr.read(), '(0... 1023)')
    print ('Helligkeit= ',ldr.prozent(),' %')
