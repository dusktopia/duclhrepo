import serial
import time

# PowerSupply = serial.Serial(port='COM10',
#                         baudrate=9600,
#                         bytesize=serial.EIGHTBITS,
#                         parity=serial.PARITY_NONE,
#                         stopbits=serial.STOPBITS_TWO,
#                         timeout=5)

class PowerSupply(serial.Serial):

    def serial_send_data(self, request:str, delay=0.2):
        self.write(bytes(request+'\n', encoding='ascii'))
        time.sleep(delay)

    def serial_receive_data(self):
        ret = False
        receive_data = ''
        time.sleep(1)
        buffer_size = self.in_waiting
        if buffer_size:
            receive_data = self.read(buffer_size).decode(errors='backslashreplace')
        ret = receive_data
        return ret
    
    def power_supply_init(self):
        self.serial_send_data('SYST:REM')
        self.serial_send_data('OUTP 1')
        self.serial_send_data('OUTP OFF')
        self.serial_send_data('INST OUTP1')
        self.serial_send_data('VOLT 12')
        self.serial_send_data('CURR 5')

    def power_off(self):
        self.serial_send_data('OUTP 1')
        self.serial_send_data('OUTP OFF')

    def power_on(self):
        self.serial_send_data('OUTP 1')
        self.serial_send_data('OUTP ON')

    def power_reset(self):
        self.serial_send_data('OUTP 1')
        self.serial_send_data('OUTP OFF')
        self.serial_send_data('OUTP ON')  

    def power_set_volt(self, channel:int, voltage:int):
        if 0 <= voltage <= 12:
            output = {1: 'INST OUTP1', 2: 'INST OUTP2'}
            self.serial_send_data(output[channel])
            self.serial_send_data('VOLT {volt}'.format(volt=voltage))
        else:
            pass

    def power_set_curr(self, channel:int, current:int):
        if 0 <= current <= 5:
            output = {1: 'INST OUTP1', 2: 'INST OUTP2'}
            self.serial_send_data(output[channel])
            self.serial_send_data('CURR {curr}'.format(curr=current))
        else:
            pass

    def power_control(self, option:str):
        pass

if __name__ == '__main__':
    E3632A_Device = PowerSupply(port='COM10', baudrate=9600,
                        bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_TWO,
                        timeout=1)
    time.sleep(5)
    E3632A_Device.power_supply_init()
    data = E3632A_Device.serial_receive_data()
    print('data = ', data)
    
