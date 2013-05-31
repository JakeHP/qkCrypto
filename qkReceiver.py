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
        self.sharedResults = []
        self.sharedKey = []

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
        return

    #Simply exists for ease of understanding
    def receive(self, arg1):
        self.measurePolarizations(arg1)
        return

    #Measure and record all polarizations from photon pulse in the comm channel
    def measurePolarizations(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg'
        if len(insecureCommChannel.photonPulse) != self.PHOTON_PULSE_SIZE:
            print("CommChannel has no photons for receiver || CommChannel # of pulses != receivers photon_pulse_size")
            return -1
        self.setRandomBasis()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            tempPho = insecureCommChannel.photonPulse[i]
            assert isinstance(tempPho, qkPhoton.qkPhoton) , 'Not a qkPhoton object - Error'
            self.recordedPolarizations.append(tempPho.measure(self.randomBasis[i]))
            i+=1
        insecureCommChannel.photonPulse.clear()
        return

    #Retrieve sender basis's and check against local random basiss
    def checkSenderBasis(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel) , 'Invalid Arg'
        #Retrieve & Remove sender basis from communication channel
        if self.PHOTON_PULSE_SIZE == len(insecureCommChannel.basisCheck):
            self.checkBasis = insecureCommChannel.basisCheck.copy()
            insecureCommChannel.basisCheck.clear()

    #Compare sent and received basis
    def compareBasis(self):
        print("RcheckBasis: ",len(self.checkBasis))
        print("RrandomBasis",len(self.randomBasis))
        print("RrecordedPolars",len(self.recordedPolarizations))
        if len(self.checkBasis) == self.PHOTON_PULSE_SIZE and len(self.randomBasis) == self.PHOTON_PULSE_SIZE and len(self.recordedPolarizations) == self.PHOTON_PULSE_SIZE:
            i = 0
            count = 0
            while i < self.PHOTON_PULSE_SIZE:
                if self.randomBasis[i] == self.checkBasis[i]:
                    count+=1
                i+=1
            print("Number Of Similar Basis: ", count, "/", self.PHOTON_PULSE_SIZE)

    #Prints all data
    def printAll(self):
        print ("qkReceiver recordedPolars: ",self.recordedPolarizations)
        print ("qkReceiver randomBasis: ",self.randomBasis)
        print ("qkReceiver checkBasis: ",self.checkBasis)