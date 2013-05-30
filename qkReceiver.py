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
        self.checkBasis = []

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

    #Simply exists for ease of understanding
    def receive(self, arg1):
        self.measurePolarizations(arg1)

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

    #Retrieve sender basis's and check against local random basiss
    def checkSenderBasis(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg'
        #Retrieve & Remove sender basis from communication channel
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            self.checkBasis.append(insecureCommChannel.basisCheck.pop())
            i+=1
        #Generate own random basis's
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            x = randint(0,1)
            if x == 0:
                self.randomBasis.append("R")
            else:
                self.randomBasis.append("D")
            i+=1

    def printAll(self):
        print ("qkReceiver recordedPolars: ",self.recordedPolarizations)
        print ("qkReceiver randomBasis: ",self.randomBasis)
        print ("qkReceiver checkBasis: ",self.checkBasis)