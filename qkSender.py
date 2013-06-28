__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton
import qkComm


#will extend qkComm in the future
class qkSender(qkComm):

    def __init__(self):
        self.photonPulse = []
        self.randomBasis = []
        self.otherBasis = []
        self.photonPolars = []
        self.sharedKey = []
        self.subSharedKey = []
        self.decision = -1
        self.otherDecision = -1
        self.validKey = -1

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

    #Send a photon pulse
    def send(self, insecureChannel, pPulse):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureChannel.photonPulse = pPulse

    #Send a basis to a specified qkCommChannel
    def sendBasis(self, insecureChannel, basisC):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureChannel.basisCheck = basisC

    #Prints All Data
    def printAll(self):
        print("qkSender Photon Pulse:          ", self.photonPulse)
        print("qkSender Photon Polarizations:  ", self.photonPolars)
        print("qkSender Basis:                 ", self.randomBasis)
        print("Receiver's Basis:               ", self.otherBasis)
        print("qkSender's sharedKey:           ", self.sharedKey)
        print("qkSender's sharedKey:           ", self.subSharedKey)

    #Prints Lengths Of Data
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