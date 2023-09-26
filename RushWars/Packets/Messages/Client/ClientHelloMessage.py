from Utils.Reader import Reader
from Packets.Messages.Server.ServerHelloMessage import *


class ClientHelloMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        self.Protocol = self.readUInt32()
        self.KeyVersion = self.readUInt32()
        self.MajorVersion = self.readUInt32()
        self.BuildVersion = self.readUInt32()
        self.ContentVersion = self.readUInt32()
        self.Hash = self.readString()
        self.Device = self.readUInt32()
        self.Store = self.readUInt32()

    def process(self):
        print(f"\n------------------------------\n[*] Received Session Data:\n------------------------------\nProtocol: {self.Protocol}\nPepperKeyVersion: {self.KeyVersion}\nGameVersion: {self.MajorVersion}\nGameBuild: {self.BuildVersion}\nContentVersion: {self.ContentVersion}\nHash: {self.Hash}\nDevice: {self.Device}\nStore: {self.Store}\n------------------------------\n")

        ServerHelloMessage(self.device).Send()