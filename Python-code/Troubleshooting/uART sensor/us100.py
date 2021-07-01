import time
import serial

uart = serial.Serial("/dev/ttyAMA1", baudrate=9600, timeout=1)

def distance(uart):
    for _ in range(2):
        uart.write(bytes([0x55]))
        time.sleep(0.1)
        data = uart.read(2) 
        if data:  
            break
        time.sleep(0.1)  
    else:
        return None

    if len(data) != 2:
        return None

    dist = (data[1] + (data[0] << 8)) / 10
    return dist


while True:
    print("-----")
    print("Distance: ", distance(uart))
    time.sleep(0.5)

