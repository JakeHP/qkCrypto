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
        self.senderBasis = []
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

    def setBitString(self):
        if 0 < len(self.recordedPolarizations) < self.PHOTON_PULSE_SIZE:
            print("TODO")
        else:
            print("Error - Photon Polars Size Is Incorrect.")

    def getSubBitString(self, insecureChannel):
        self.subSharedKey.clear()
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        if len(insecureChannel.subSharedKey) > 0:
            self.subSharedKey = insecureChannel.subSharedKey.copy()
            insecureChannel.subSharedKey.clear()
        else:
            print("Error - qkCommChannel has no bit sub string.")

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
            self.senderBasis = insecureCommChannel.basisCheck.copy()
            insecureCommChannel.basisCheck.clear()

    #Compare sent and received basis
    def compareBasis(self):
        if len(self.senderBasis) == self.PHOTON_PULSE_SIZE and len(self.randomBasis) == self.PHOTON_PULSE_SIZE and len(self.recordedPolarizations) == self.PHOTON_PULSE_SIZE:
            i = 0
            count = 0
            while i < self.PHOTON_PULSE_SIZE:
                if self.randomBasis[i] == self.senderBasis[i]:
                    count += 1
                i += 1
            print("Number Of Similar Basis: ", count, "/", self.PHOTON_PULSE_SIZE)

    #Send basis to a qkCommChannel for a sender/Alice
    def sendBasis(self, insecureChannel, basisC):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureChannel.basisCheck = basisC

    def dropInvalidPolars(self):
        if len(self.senderBasis) == self.PHOTON_PULSE_SIZE and len(self.randomBasis) == self.PHOTON_PULSE_SIZE and len(self.recordedPolarizations) == self.PHOTON_PULSE_SIZE:
            i = 0
            max = self.PHOTON_PULSE_SIZE
            while i < max:
                if self.randomBasis[i] != self.senderBasis[i]:
                    self.randomBasis.pop(i)
                    self.senderBasis.pop(i)
                    self.recordedPolarizations.pop(i)
                    max -= 1
                else:
                    i += 1
        else:
            print("Error - Required Data Not Initialized.")
        print("R - Number Of Basis Left: ",len(self.randomBasis))

    #Prints all data
    def printAll(self):
        print ("qkReceiver recordedPolars:      ",self.recordedPolarizations)
        print ("qkReceiver Random Basis:        ",self.randomBasis)
        print ("Sender's Basis:                 ",self.senderBasis)

    def printDetails(self):
        print ("qkSender Photon Polarizations:  ",len(self.recordedPolarizations))
        print ("qkSender Random Basis:          ",len(self.randomBasis))
        print ("Receiver's Basis:               ",len(self.senderBasis))