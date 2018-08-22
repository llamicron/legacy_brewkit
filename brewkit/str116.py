import time
import serial

class STR116(object):
    def __init__(self, address = 2, port = '/dev/ttyAMA0'):
        self.address = address
        self.port = port

        self.baudRate = 19200
        self.timeout = 0.05

        self.settings = {
            #master start byte
            'MA0': '55',
            #master1 byte
            'MA1': 'AA',
            #master end byte
            'MAE': '77',
            #hex byte for controller number
            'CN': '02'
        }

    def get_checksum(self, data):
        checksum = sum(bytearray.fromhex(data))
        checksumstripped = hex(checksum).replace('0x', '')
        return checksumstripped.zfill(2)

    def write_message(self, data):
        try:
            usart = serial.Serial(self.port, self.baudRate)
        except IOError as e:
            print(("Failed to create serial object. ({})".format(e)))

        usart.timeout = self.timeout
        # message_bytes = data.decode("hex")
        message_bytes = data
        try:
            usart.write(message_bytes)
        except IOError as e:
            print(("Failed to write to the port. ({})".format(e)))

    def write_message_with_response(self, data):
        usart = serial.Serial(self.port, self.baudRate)
        usart.timeout = self.timeout
        message_bytes = data.decode("hex")
        try:
            usart.write(message_bytes)
            #print usart.open  # True for opened
            if usart.open:
                time.sleep(0.02)
                size = usart.inWaiting()
                if size:
                    data = usart.read(size)
                    # print binascii.hexlify(data)
                else:
                    print('no data')
            else:
                print('usart not open')
        except IOError as e:
            print(("Failed to write to the port. ({})".format(e)))
        return binascii.hexlify(data)

    def get_relay(self, relay_number):
        '''Get the status of the requested relay (true/false)'''
        time.sleep(0.005)
        str_to_checksum = '0714' + self.settings['CN'] + '0010'
        CS = self.get_checksum(str_to_checksum)
        bytestring = self.settings['MA0'] + self.settings['MA1'] + str_to_checksum \
            + str(CS) + self.settings['MAE']
        relaystatus = self.write_message_with_response(bytestring)[6:-4]
        test = relaystatus[relay_number*2:relay_number*2+2]
        return int(test)

    def set_relay(self, relay_number, state):
        #command to turn on relay is 0x08 0x17
        #format is
        #MA0, MA1, 0x08, 0x17, CN, start number output (relaynumber), \
        #number of outputs (usually 0x01), 00/01 (off/on), CS (calculated), MAE
        #need to do a checksum on 0x08, 0x17, CN, relaynumber, 0x01, 0x01

        relaynumberhex = hex(relay_number).replace('0x', '').zfill(2)
        str_to_checksum = '0817' + self.settings['CN'] + str(relaynumberhex) \
            + '01' + str(state).zfill(2)
        CS = self.get_checksum(str_to_checksum)
        bytestring = self.settings['MA0'] + self.settings['MA1'] + str_to_checksum \
            + str(CS) + self.settings['MAE']
        self.write_message(bytestring)
