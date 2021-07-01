import time

class TMP36:

    def __init__(self, spi):
        self._spi = spi
    
    @property
    def temperature(self):
        channel = 1
        adc = self._spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        
        temp = ((data * 330)/float(1023))-50
        temp = round(temp,2)
        return temp