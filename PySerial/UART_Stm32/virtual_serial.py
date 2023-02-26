import serial
import time

# * COM Port configuration
# * Modify in server

UDSDataBase = {
    'SID': {
        '0x10': 'diagnostic_session_control',
        '0x11': 'ecu_reset',
        '0x27': 'security_access',
        '0x28': 'communication_control',
        '0x29': 'authentication',
        '0x3E': 'tester_present',
        '0x83': 'access_timing_parameters',
        '0x84': 'secured_data_transmission',
        '0x85': 'control_dtc_settings',
        '0x86': 'response_on_event',
        '0x87': 'link_control'
    },
    'Sub_function': {
        '0x00': 'unsupported',
        '0x01': 'supported'
    },
    'DID': {
        '0x00': 'unsupported',
        '0x01': 'supported'        
    }
}

vserial = serial.Serial(port='COM10',
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=2)

while True:
    buffer = vserial.in_waiting
    if buffer:
        req_msg = vserial.read(buffer)
        req_msg = req_msg.decode()
        req_msg = req_msg.replace('\n', '')
        if req_msg == 'Terminate':
            break
        # elif req_msg in UDSDataBase['SID']:
        #     service = UDSDataBase['SID'][req_msg] + '\n'
        #     print(service, end='')
        #     vserial.write(service.encode())
        # else:
        #     service = 'Invalid service ID\n'
        #     vserial.write(service.encode())
        else:
            byte = req_msg.split()
            print(UDSDataBase['SID'][byte[0]])
            print(UDSDataBase['Sub_function'][byte[1]])
            print(UDSDataBase['DID'][byte[2]])

vserial.close()
