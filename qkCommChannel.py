__author__ = 'Jakehp'


#Kind of a useless class, all data is passed through here, so an attacker has the ability to see what's going on
#senders, receivers, and attackers manage transmitting the data to and from qkCommChannel
class qkCommChannel:

    def __init__(self):
        self.photonPulse = []
        self.basisCheck = []
        self.subSharedKey = []

    def printAll(self):
        print ("qkCommChannel PhotonPulse:      ",self.photonPulse)
        print ("qkCommChannel basisCheck:       ",self.basisCheck)