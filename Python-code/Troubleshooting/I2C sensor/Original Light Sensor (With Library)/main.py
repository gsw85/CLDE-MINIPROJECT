import Lib
import time
import smbus

i2c = smbus.SMBus(1)
sensor_light = Lib.BH1750FVI(i2c)

while True:
    lightLevel=sensor_light.lux
    print("Light Level : ", format(lightLevel,'.2f'))
    time.sleep(0.5)

