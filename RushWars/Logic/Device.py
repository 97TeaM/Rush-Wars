import traceback
from Packets.MessageFactory import *


class Device:

    AndroidID = None
    DeviceModel = None
    OpenUDID = None
    OSVersion = None
    IsAndroid = False
    Language = None

    def __init__(self, socket=None):
        self.socket = socket

    def SendData(self, ID, data, version=None):
        packetID = ID.to_bytes(2, "big")

        if version:
            packetVersion = version.to_bytes(2, "big")
        else:
            packetVersion = (0).to_bytes(2, "big")
        if self.socket is None:
            self.transport.write(packetID + len(data).to_bytes(3, "big") + packetVersion + data)
        else:
            self.socket.send(packetID + len(data).to_bytes(3, "big") + packetVersion + data)

        print(f"[*] {ID} sent")

    def decrypt(self, data):
        return self.crypto.decrypt(data)

    def processPacket(self, packetID, payload):

        print(f"[*] {packetID} received")

        try:
            if packetID in availablePackets:

                Message = availablePackets[packetID](payload, self)
                Message.decode()
                Message.process()
            else:
                print(f"[*] {packetID} not handled")
        except:
            print(f"[*] Error while decrypting / handling {packetID}")
            traceback.print_exc()