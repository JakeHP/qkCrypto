__author__ = 'Jakehp'
from random import randint
import qkPhoton
import qkCommChannel



#Receivers *cannot* access any photons - except via measurement
class qkReceiver:

    PHOTON_PULSE_SIZE = 128

    def __init__(self):
        self.recordedPolarizations = []
        self.randomBasis = []

    #Computes random basis's for randomBasis list
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
        if len(insecureCommChannel.photonPulse) != self.PHOTON_PULSE_SIZE:
            print("CommChannel has no photons for receiver || CommChannel # of pulses != receivers photon_pulse_size")
            return -1
        self.setRandomBasis()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            tempPho = insecureCommChannel.photonPulse.pop()
            assert isinstance(tempPho, qkPhoton.qkPhoton) , 'Not a qkPhoton object - Error'
            self.recordedPolarizations.append(tempPho.measure(self.randomBasis.pop()))
            i+=1

    #receive alice/sender basis's, get all same basis, check for differences in polarization - if so % bit difference -> MITM has measured
    #def checkBasis(self, insecureCommChannel):

    def printAll(self):
        print ("qkReceiver recordedPolars: ",self.recordedPolarizations)
        print ("qkReceiver randomBasis: ",self.randomBasis)