__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton
import qkPhotonPulse

class qkSender:

    def __init__(self):
        self.photonPulse = []
        self.basisCheck = []

    def createPhotonPulse(self):
        self.photonPulse.clear()
        self.basisCheck.clear()
        i = 0
        while i<128:
            self.photonPulse.append(self.createPhoton())
            i+=1

    def createPhoton(self):
        data = qkPhoton.qkPhoton()
        data.setRandomBit()
        basis = data.setRandomBasis()
        self.basisCheck.append(basis)
        data.setPolarization()
        return data

    def send(self, insecureChannel, ppulse):
        assert isinstance(insecureChannel, qkCommChannel)
        insecureChannel.qkCommChannel.photonPulse = ppulse

    def sendBasisChecks(self, insecureChannel, basisC):
        assert isinstance(insecureChannel, qkCommChannel)
        insecureChannel.qkCommChannel.basicChecks = basisC

    def printAll(self):
        print (self.photonPulse)
        print (self.basisCheck)