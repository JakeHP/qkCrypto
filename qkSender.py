__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton

#will extend qkComm in the future

class qkSender:

    PHOTON_PULSE_SIZE = 128

    def __init__(self):
        self.photonPulse = []
        self.randomBasis = []
        self.basis = []
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
        self.basis.clear()
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg'
        #Retrieve & Remove sender basis from communication channel
        if self.PHOTON_PULSE_SIZE == len(insecureCommChannel.basisCheck):
            self.basis = insecureCommChannel.basisCheck.copy()
            insecureCommChannel.basisCheck.clear()

    def dropInvalidPolars(self):
        if len(self.basis) == self.PHOTON_PULSE_SIZE and len(self.randomBasis) == self.PHOTON_PULSE_SIZE and len(self.photonPulse) == self.PHOTON_PULSE_SIZE and len(self.photonPolars) == self.PHOTON_PULSE_SIZE:
            i = 0
            max = self.PHOTON_PULSE_SIZE
            while i < max:
                if self.randomBasis[i] != self.basis[i]:
                    self.randomBasis.pop(i)
                    self.basis.pop(i)
                    self.photonPolars.pop(i)
                    self.photonPulse.pop(i)
                    max -= 1
                else:
                    i += 1
        else:
            print("Error - Required Data Not Initialized.")
        print("S - Number Of Basis Left: ",len(self.basis))

    def printAll(self):
        print ("qkSender Photon Pulse:          ",self.photonPulse)
        print ("qkSender Photon Polarizations:  ",self.photonPolars)
        print ("qkSender Basis:                 ",self.randomBasis)
        print ("Receiver's Basis:               ",self.basis)

    def printDetails(self):
        print ("qkSender Photon Pulse:          ",len(self.photonPulse))
        print ("qkSender Photon Polarizations:  ",len(self.photonPolars))
        print ("qkSender Random Basis:          ",len(self.randomBasis))
        print ("Receiver's Basis:               ",len(self.basis))