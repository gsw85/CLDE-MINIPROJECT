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

class BH1750FVI:

    def __init__(self, i2c):
        self._i2c = i2c
    
    @property
    def lux(self):
        
        data = self._i2c.read_i2c_block_data(DEVICE,ONE_TIME_HIGH_RES_MODE_1)
        result=(data[1] + (256 * data[0])) / 1.2
        return (result)