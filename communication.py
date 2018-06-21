import serial
from xbee import XBee


class XBeeComm:

    def __init__(self, com='COM3', baud=9600):
        #self.xbee = XBee(serial.Serial(com,baud))
        pass
        
    def tx(self, data, dest='\x00\x01'):
        print(data); return
        #self.xbee.tx(dest_addr=dest,data=data)


class Packets:

    def __init__(self):
        self.data = []

    def push(self, data):

        if type(data) is tuple:
            for i in data:
                self.push(i)
            return

        data = str(data)
        if data.isdigit():
            data = data + '|'

        self.data.append(data)

    def resetData(self):
        self.data = []

    def createPacket(self):
        packet = '<' + ''.join(self.data) + '>'
        return packet