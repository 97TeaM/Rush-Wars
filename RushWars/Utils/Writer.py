import zlib


class Writer:
    def __init__(self, client, endian: str = "big"):
        self.client = client
        self.endian = endian
        self.buffer = b""

    def writeInt(self, data, length=4):
        self.buffer += data.to_bytes(length, "big")

    def writeLogicLong(self, x, y):
        self.writeInt(x)
        self.writeInt(y)

    def writeIntLittleEndian(self, data, length=4):
        self.buffer += data.to_bytes(length, "little")

    def writeUInteger(self, integer: int, length: int = 1):
        self.buffer += integer.to_bytes(length, self.endian, signed=False)

    def writeUInt8(self, integer: int):
        self.writeUInteger(integer)
    
    def writeByte(self, data):
        self.writeInt(data, 1)

    def writeBytes(self, data):
        self.buffer += data

    def writeBoolean(self, boolean: bool):
        if boolean:
            self.writeUInt8(1)
        else:
            self.writeUInt8(0)

    def writeHexa(self, data):
        if data:
            if data.startswith("0x"):
                data = data[2:]
            self.buffer += bytes.fromhex("".join(data.split()).replace("-", ""))

    def writeVInt(self, data, rotate: bool = True):
        final = b""
        if data == 0:
            self.writeByte(0)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f

                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)

                final += b.to_bytes(1, "big")
                data >>= 7
        self.buffer += final

    def writeArrayVInt(self, data):
        for x in data:
            self.writeVInt(x)

    def writeLong(self, x, y):
        self.writeVInt(x)
        self.writeVInt(y)
    
    def writeDataSlot(self, x, y, data):
        self.writeLogicLong(x, y)
        self.writeVInt(data)

    def writeString(self, string: str = None):
        if string is not None:
            encoded = string.encode("utf-8")
            self.writeInt(len(encoded))
            self.buffer += encoded
        else:
            self.writeInt(2 ** 32 - 1)

    def writeCompressedString(self, bytes: bytes = None):
        if bytes is not None:
            compessed = zlib.compress(bytes)
            self.writeInt(len(compessed) + 4)
            self.writeIntLittleEndian(len(bytes))
            self.buffer += compessed

    def Send(self):
        self.encode()
        if hasattr(self, "version"):
            self.device.SendData(self.id, self.buffer, self.version)
        else:
            self.device.SendData(self.id, self.buffer)