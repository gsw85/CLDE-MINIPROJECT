import Lib
import time
import spidev
import os

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

sensor_temperature = Lib.TMP36(spi)

while True:
        
    temp_level=sensor_temperature.temperature
    print ("--------------------------------------------")
    print("Temp : ", format(temp_level))
    time.sleep(0.5)