import serial
import time

master = serial.Serial(port='COM3',
                       baudrate=9600,
                       bytesize=serial.EIGHTBITS,
                       parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE,
                       timeout=2)

led_on = bytes('LED ON\n', encoding='ascii')
led_off = bytes('LED OFF\n', encoding='ascii')

for i in range(3):
    master.write(led_on)
    time.sleep(3)
    master.write(led_off)
    time.sleep(3)

master.close()
