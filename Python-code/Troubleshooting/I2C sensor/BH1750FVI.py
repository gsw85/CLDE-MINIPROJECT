import smbus
import time

# Define some constants from the datasheet
DEVICE                      = 0x23  # Default device I2C address which addr pins connected to ground
POWER_DOWN                  = 0x00  # No active state
POWER_ON                    = 0x01  # Waiting for measurement command
RESET                       = 0x07  # Reset data register value

CONTINUOUS_HIGH_RES_MODE_1  = 0x10  # Start measurement at 1lx resolution. Measurement Time is typically 120ms.
CONTINUOUS_HIGH_RES_MODE_2  = 0x11  # Start measurement at 0.5lx resolution. Measurement Time is typically 120ms.
CONTINUOUS_LOW_RES_MODE     = 0x13  # Start measurement at 4lx resolution. Measurement Time is typically 16ms.

ONE_TIME_HIGH_RES_MODE_1    = 0x20  # Start measurement at 1lx resolution. Measurement Time is typically 120ms.
ONE_TIME_HIGH_RES_MODE_2    = 0x21  # Start measurement at 0.5lx resolution. Measurement Time is typically 120ms.
ONE_TIME_LOW_RES_MODE       = 0x23  # Start measurement at 4lx resolution. Measurement Time is typically 16ms.

#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
  # Read data from I2C interface
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)

def main():

  while True:
    lightLevel=readLight()
    print("Light Level : " + format(lightLevel,'.2f') + " lx")
    time.sleep(0.5)

if __name__=="__main__":
   main()