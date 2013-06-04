__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton

class qkSender:

    PHOTON_PULSE_SIZE = 128

    def __init__(self):
        self.photonPulse = []
        self.randomBasis = []
        self.basis = []
        self.photonPolars = []

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

    def send(self, insecureChannel, pPulse):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureChannel.photonPulse = pPulse

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

    def printAll(self):
        print ("qkSender Photon Pulse:          ",self.photonPulse)
        print ("qkSender Photon Polarizations:  ",self.photonPolars)
        print ("qkSender Basis:                 ",self.randomBasis)
        print ("Receiver's Basis:               ",self.basis)