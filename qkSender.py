__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton

#will extend qkComm in the future

class qkSender:

    PHOTON_PULSE_SIZE = 128

    def __init__(self):
        self.photonPulse = []
        self.randomBasis = []
        self.otherBasis = []
        self.photonPolars = []
        self.sharedKey = []
        self.subSharedKey = []

    def createPhotonPulse(self):
        self.photonPulse.clear()
        self.randomBasis.clear()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            self.photonPulse.append(self.createPhoton())
            i += 1

    def createPhoton(self):
        data = qkPhoton.qkPhoton()
        data.setRandomBit()
        basis = data.setRandomBasis()
        self.randomBasis.append(basis)
        polar = data.setPolarization()
        self.photonPolars.append(polar)
        return data

    def setBitString(self):
        if 0 < len(self.recordedPolarizations) < self.PHOTON_PULSE_SIZE:
            print("TODO")
        else:
            print("Error - Photon Polars Size Is Incorrect.")

    def getSubBitString(self, insecureChannel):
        self.subSharedKey.clear()
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        if len(insecureChannel.subSharedKey) > 0:
            self.subSharedKey = insecureChannel.subSharedKey.copy()
            insecureChannel.subSharedKey.clear()
        else:
            print("Error - qkCommChannel has no bit sub string.")

    def send(self, insecureChannel, pPulse):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureChannel.photonPulse = pPulse

    #Send a basis to a specified qkCommChannel
    def sendBasis(self, insecureChannel, basisC):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureChannel.basisCheck = basisC

    #Retrieve sender basis's and check against local random basiss
    def checkReceiverBasis(self, insecureCommChannel):
        self.otherBasis.clear()
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg'
        #Retrieve & Remove sender basis from communication channel
        if self.PHOTON_PULSE_SIZE == len(insecureCommChannel.basisCheck):
            self.otherBasis = insecureCommChannel.basisCheck.copy()
            insecureCommChannel.basisCheck.clear()

    def dropInvalidPolars(self):
        if len(self.otherBasis) == self.PHOTON_PULSE_SIZE and len(self.randomBasis) == self.PHOTON_PULSE_SIZE and len(self.photonPulse) == self.PHOTON_PULSE_SIZE and len(self.photonPolars) == self.PHOTON_PULSE_SIZE:
            i = 0
            max = self.PHOTON_PULSE_SIZE
            while i < max:
                if self.randomBasis[i] != self.otherBasis[i]:
                    self.randomBasis.pop(i)
                    self.otherBasis.pop(i)
                    self.photonPolars.pop(i)
                    self.photonPulse.pop(i)
                    max -= 1
                else:
                    i += 1
        else:
            print("Error - Required Data Not Initialized.")
        print("S - Number Of Basis Left: ", len(self.otherBasis))

    def setBitString(self):
        self.sharedKey.clear()
        if len(self.photonPolars) <= self.PHOTON_PULSE_SIZE and len(self.photonPolars) > 0:
            i = 0
            while i < len(self.photonPolars):
                if self.photonPolars[i] == 0:
                    self.sharedKey.append(0)
                elif self.photonPolars[i] == 90:
                    self.sharedKey.append(1)
                elif self.photonPolars[i] == 45:
                    self.sharedKey.append(0)
                elif self.photonPolars[i] == 135:
                    self.sharedKey.append(1)
                i += 1

    def sendSubBitString(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureCommChannel.subSharedKey.clear()
        if len(self.sharedKey) > 0:
            insecureCommChannel.subSharedKey = (self.sharedKey[0: (int((len(self.sharedKey))/2))]).copy()

    def getSubBitString(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        self.subSharedKey.clear()
        if len(insecureCommChannel.subSharedKey) > 0:
            self.subSharedKey = insecureCommChannel.subSharedKey.copy()
            insecureCommChannel.subSharedKey.clear()
        else:
            print("Error - CommChannel's Sub Shared Key Is Empty!")

    def printAll(self):
        print("qkSender Photon Pulse:          ", self.photonPulse)
        print("qkSender Photon Polarizations:  ", self.photonPolars)
        print("qkSender Basis:                 ", self.randomBasis)
        print("Receiver's Basis:               ", self.otherBasis)
        print("qkSender's sharedKey:           ", self.sharedKey)
        print("qkSender's sharedKey:           ", self.subSharedKey)

    def printDetails(self):
        print("qkSender Photon Pulse:          ", len(self.photonPulse))
        print("qkSender Photon Polarizations:  ", len(self.photonPolars))
        print("qkSender Random Basis:          ", len(self.randomBasis))
        print("Receiver's Basis:               ", len(self.otherBasis))

    def compareTwoArrays(self, arg1, arg2):
        test = 0
        if len(arg1) != len(arg2):
            print("Two Arrays - Not Equal!")
        else:
            i = 0
            while i < len(arg1):
                if arg1[i] != arg2[i]:
                    test = 1
                i += 1
            if test == 0:
                print("Two Arrays - Equal!")
            else:
                print("Two Arrays - Not Equal!")