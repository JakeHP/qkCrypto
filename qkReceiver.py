__author__ = 'Jakehp'
from random import randint
import qkPhoton
import qkCommChannel
import qkComm

#will extend qkComm in the future
#Receivers *cannot* access any photons - except via measurement
class qkReceiver(qkComm.qkComm):

    PHOTON_PULSE_SIZE = 128
    MIN_REQ_OF_SHARED = 25

    def __init__(self):
        self.recordedPolarizations = []
        self.randomBasis = []
        self.otherBasis = []
        self.sharedKey = []
        self.subSharedKey = []
        self.decision = -1
        self.otherDecision = -1
        self.validKey = -1

    #Computes random basis's for randomBasis list
    def setRandomBasis(self):
        self.randomBasis.clear()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            x = randint(0, 1)
            if x == 0:
                self.randomBasis.append("R")
            else:
                self.randomBasis.append("D")
            i += 1
        return

    #Simply exists for ease of understanding
    def receive(self, arg1):
        self.measurePolarizations(arg1)
        return

    #Measure and record all polarizations from photon pulse in the comm channel
    def measurePolarizations(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg'
        if len(insecureCommChannel.photonPulse) != self.PHOTON_PULSE_SIZE:
            print("CommChannel has no photons for receiver || CommChannel # of pulses != receivers photon_pulse_size")
            return -1
        self.setRandomBasis()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            tempPho = insecureCommChannel.photonPulse[i]
            assert isinstance(tempPho, qkPhoton.qkPhoton), 'Not a qkPhoton object - Error'
            self.recordedPolarizations.append(tempPho.measure(self.randomBasis[i]))
            i += 1
        insecureCommChannel.photonPulse.clear()
        return

    #Prints All Data
    def printAll(self):
        print("qkReceiver recordedPolars:      ", self.recordedPolarizations)
        print("qkReceiver Random Basis:        ", self.randomBasis)
        print("Sender's Basis:                 ", self.otherBasis)
        print("qkReceiver's sharedKey:         ", self.sharedKey)
        print("qkReceiver's subSharedKey:      ", self.subSharedKey)

    #Prints Lengths Of Data
    def printDetails(self):
        print("qkSender Photon Polarizations:  ", len(self.recordedPolarizations))
        print("qkSender Random Basis:          ", len(self.randomBasis))
        print("Receiver's Basis:               ", len(self.otherBasis))