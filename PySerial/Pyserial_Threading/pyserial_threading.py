import serial
import curses
import threading
import signal
import sys

global uart
uart = True

scr = curses.initscr()
scr.refresh()
row, col = 0, 0
scr.addstr(row, col, 'Data: ')
scr.addstr(row+3, col, 'Press q to quit the program.')

def signal_handler(signum, frame):
    sys.exit()

def controlSerial():
    global uart
    ser = serial.Serial(port = 'COM3', baudrate=9600, bytesize=8, timeout=2,
                        stopbits=serial.STOPBITS_ONE)
    while uart:
        data = ser.readline()
        data_sensor = data.decode('utf8')
        scr.addstr(row, col+8, data_sensor)
        scr.refresh()

serial_handler = threading.Thread(target=controlSerial)
serial_handler.daemon = True
serial_handler.start()

signal.signal(signal.SIGINT, signal_handler)

while True:
    key_press = scr.getkey()
    if key_press == 'q':
        uart = False
        break