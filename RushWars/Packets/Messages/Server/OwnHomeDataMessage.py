from Utils.Writer import Writer


class OwnHomeDataMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24101

    def encode(self):
        self.writeVInt(0)
        self.writeLogicLong(0, 1) # id

        self.writeCompressedString("{\"locations\":[{\"objs\":{\"gameobjects\":[{\"id\":6000000,\"data\":32000000,\"go\":{\"pos_x\":12000,\"pos_y\":8000,\"components\":[]}},{\"id\":6000001,\"data\":32000001,\"go\":{\"pos_x\":5000,\"pos_y\":9500,\"components\":[]}},{\"id\":6000005,\"data\":32000004,\"go\":{\"pos_x\":5000,\"pos_y\":9500,\"components\":[]}},{\"id\":6000002,\"data\":32000002,\"go\":{\"pos_x\":19500,\"pos_y\":9500,\"components\":[]}},{\"id\":6000003,\"data\":32000003,\"go\":{\"pos_x\":10750,\"pos_y\":17000,\"components\":[]}},{\"id\":6000004,\"data\":32000003,\"go\":{\"pos_x\":13250,\"pos_y\":17000,\"components\":[]}}]},\"loc\":15000000}]}")  # homejson

        self.writeLong(0, 1)  # id
        self.writeLong(0, 1)  # id

        self.writeString("Solar")  # name
        self.writeVInt(0)
        self.writeBoolean(True) # name set
        self.writeVInt(-1)
        self.writeVInt(0)

        self.writeVInt(21)
        for i in range(21):
            self.writeVInt(7)  # data slots
            for i in range(7):
                self.writeDataSlot(5, 1, 9999999)  # gold
                self.writeDataSlot(5, 2, 9999999)  # freegold
                self.writeDataSlot(5, 3, 9999999)  # mineral
                self.writeDataSlot(5, 4, 9999999)  # freemineral
                self.writeDataSlot(5, 6, 6)  # keys
                self.writeDataSlot(5, 8, 10000)  # stars

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)  # is in alliance

        self.writeVInt(50)  # exp level
        self.writeVInt(0)  # exp points
        self.writeVInt(9999999)  # diamonds
        self.writeVInt(0)  # free diamonds
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # score
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(-1)

        self.writeVInt(0)  # another slots count