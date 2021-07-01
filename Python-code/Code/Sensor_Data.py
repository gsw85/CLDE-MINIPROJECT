import time
import serial
import smbus
import spidev
import os
import Library

uart = serial.Serial("/dev/ttyAMA1", baudrate=9600, timeout=1)
i2c = smbus.SMBus(1)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

sensor_us100 = Library.US100(uart)
sensor_light = Library.BH1750FVI(i2c)
sensor_temperature = Library.TMP36(spi)

while True:

    print("Distance:" + str(sensor_us100.distance))
    time.sleep(2)
    
    print("Light:" + str(sensor_light.lux))
    time.sleep(2)
    
    print("Temperature:" + str(sensor_temperature.temperature))
    time.sleep(2)