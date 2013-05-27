__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton

class qkSender:

    PHOTON_PULSE_SIZE = 128

    def __init__(self):
        self.photonPulse = []
        self.basisCheck = []
        self.qkCommChannelPP = []

    def createPhotonPulse(self):
        self.photonPulse.clear()
        self.basisCheck.clear()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            self.photonPulse.append(self.createPhoton())
            i+=1
        self.qkCommChannelPP = self.photonPulse.copy()

    def createPhoton(self):
        data = qkPhoton.qkPhoton()
        data.setRandomBit()
        basis = data.setRandomBasis()
        self.basisCheck.append(basis)
        data.setPolarization()
        return data

    def send(self, insecureChannel, pPulse):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg1'
        insecureChannel.photonPulse = pPulse


    def sendBasisChecks(self, insecureChannel, basisC):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg1'
        insecureChannel.basisCheck = basisC

    def printAll(self):
        print ("qkSender Photon Pulse: ",self.photonPulse)
        print ("qkSender Basis Check: ",self.basisCheck)