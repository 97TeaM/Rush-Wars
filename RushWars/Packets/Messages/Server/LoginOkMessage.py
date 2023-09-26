from Utils.Writer import Writer


class LoginOkMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 20104

    def encode(self):

        self.writeInt(0)  # AccountHighID
        self.writeInt(1)  # AccountLowID

        self.writeInt(0)  # HomeHighID
        self.writeInt(1)  # HomeLowID

        self.writeString("solar")  # PassToken
        self.writeString()  # FacebookID
        self.writeString()  # GameCenterID

        self.writeVInt(0)  # MajorVersion
        self.writeVInt(0)  # ServerBuild
        self.writeVInt(0)  # ContentVersion

        self.writeString("dev")  # ServerEnvironment

        self.writeVInt(0)  # SessionCount
        self.writeVInt(0)  # PlayTimeSeconds
        self.writeVInt(0)  # DaysSinceStartedPlaying

        self.writeString()  # FacebookAppId
        self.writeString()  # ServerTime
        self.writeString()  # AccountCreatedDate

        self.writeVInt(0)  # Tier

        self.writeString()  # GoogleServiceID