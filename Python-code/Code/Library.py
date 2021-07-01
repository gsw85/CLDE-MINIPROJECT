import time

DEVICE                      = 0x23
POWER_DOWN                  = 0x00
POWER_ON                    = 0x01
RESET                       = 0x07
CONTINUOUS_HIGH_RES_MODE_1  = 0x10
CONTINUOUS_HIGH_RES_MODE_2  = 0x11
CONTINUOUS_LOW_RES_MODE     = 0x13
ONE_TIME_HIGH_RES_MODE_1    = 0x20
ONE_TIME_HIGH_RES_MODE_2    = 0x21
ONE_TIME_LOW_RES_MODE       = 0x23



class US100:
    """Control a US-100 ultrasonic range sensor."""

    def __init__(self, uart):
        self._uart = uart

    @property
    def distance(self):
       
        for _ in range(2): 
            self._uart.write(bytes([0x55]))
            time.sleep(0.1)
            data = self._uart.read(2)
            if data: 
                break
            time.sleep(0.1)  
        else:
            return None

        if len(data) != 2:
            return None

        dist = (data[1] + (data[0] << 8)) / 10
        return dist
    
    
    
class BH1750FVI:

    def __init__(self, i2c):
        self._i2c = i2c
    
    @property
    def lux(self):
        
        data = self._i2c.read_i2c_block_data(DEVICE,ONE_TIME_HIGH_RES_MODE_1)
        result=(data[1] + (256 * data[0])) / 1.2
        return (result)
    
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