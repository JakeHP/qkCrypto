__author__ = 'Jakehp'
from random import randint
import qkCommChannel



#Receivers *cannot* access any photons - except via measurement
class qkReceiver:

    PHOTON_PULSE_SIZE = 128

    def __init__(self):
        self.recordedPolarizations = []
        self.randomBasis = []

    #setRandomBasis
    def setRandomBasis(self):
        self.randomBasis.clear()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            x = randint(0,1)
            if x == 0:
                self.randomBasis.append("R")
            else:
                self.randomBasis.append("D")
            i+=1

    #Measure and record all polarizations from photon pulse in the comm channel
    def measurePolarizations(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg'
        if len(self.receivedPolarizations) != len(self.randomBasis):
            print("Receiver's photon pulse size does not match senders/received # of polarizations")
            return 0
        if len(insecureCommChannel.photonPulse) == 0:
            print("Channel has no photons for the receiver")
            return 0


    #receive alice/sender basis's, get all same basis, check for differences in polarization - if so % bit difference -> MITM has measured
