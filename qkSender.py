__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton

class qkSender:

    PHOTON_PULSE_SIZE = 128

    def __init__(self):
        self.photonPulse = []
        self.basisCheck = []

    def createPhotonPulse(self):
        self.photonPulse.clear()
        self.basisCheck.clear()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            self.photonPulse.append(self.createPhoton())
            i+=1

    def createPhoton(self):
        data = qkPhoton.qkPhoton()
        data.setRandomBit()
        basis = data.setRandomBasis()
        self.basisCheck.append(basis)
        data.setPolarization()
        return data

    def send(self, insecureChannel, pPulse):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg'
        insecureChannel.photonPulse = pPulse

    def sendBasisChecks(self, insecureChannel, basisC):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg'
        insecureChannel.basisCheck = basisC

    #def printAll(self):
    #    print ("PP: ",self.photonPulse)
    #    print ("BC: ",self.basisCheck)