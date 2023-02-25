import serial
import time

# * COM Port configuration

vserial = serial.Serial(port='COM10',
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=2)

while True:
    buffer = vserial.in_waiting
    msg_from_terminal = vserial.read(buffer)
    if buffer:
        print(msg_from_terminal.decode())
        break

vserial.close()
