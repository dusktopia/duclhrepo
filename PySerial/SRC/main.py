import serial
import keyboard as kb
import time
import matplotlib.pyplot as plt
import random as rd

def PlotRequest(n: str):
    i = 0
    xpoints = []
    ypoints = []
    while n != 1:
        i += 1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3*n+1)
        xpoints.append(i)
        ypoints.append(n)
        plt.plot(xpoints, ypoints)
    plt.tight_layout()
    plt.grid()
    plt.show()

ser = serial.Serial(port='COM12', baudrate=9600, bytesize=8, timeout=2,
                    stopbits=serial.STOPBITS_ONE)

for waiting_time in reversed(range(5)):
    sent_msg = 'Please wait the system for {sec} seconds\n'.format(sec=waiting_time+1)
    ser.write(sent_msg.encode())
    time.sleep(1)

while True:
    recv_bytes = ser.readline()
    if recv_bytes:
        recv_msg = recv_bytes.decode()
        print('Message received:', recv_msg, end='')
        if recv_msg == "STOP\n":
            break
        elif recv_msg == 'REQUEST\n':
            PlotRequest(27)
        else:
            pass

ser.close()