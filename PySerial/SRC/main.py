import serial
import keyboard as kb
import time
import os

ser = serial.Serial(port='COM12', baudrate=9600, bytesize=8, timeout=2,
                    stopbits=serial.STOPBITS_ONE)

for i in range(5):
    sent_msg = str(i+1) + '-> Message sent by Python Script\n'
    ser.write(sent_msg.encode())
    time.sleep(1)

while True:
    recv_bytes = ser.readline()
    if recv_bytes:
        recv_msg = recv_bytes.decode()
        print(recv_msg, end='')
        if recv_msg == "STOP\n":
            break
        elif recv_msg == "REQUEST\n":
            os.chdir('C:/Users/duclh')
            ter_logger = os.popen('systeminfo').read()
            sent_msg = ter_logger
            ser.write(sent_msg.encode())
        else:
            pass

ser.close()