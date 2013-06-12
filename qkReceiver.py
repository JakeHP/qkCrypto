__author__ = 'Jakehp'
from random import randint
import qkPhoton
import qkCommChannel


#will extend qkComm in the future
#Receivers *cannot* access any photons - except via measurement
class qkReceiver:

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

    #Retrieve sender basis's and check against local random basiss
    def checkSenderBasis(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg'
        #Retrieve & Remove sender basis from communication channel
        if self.PHOTON_PULSE_SIZE == len(insecureCommChannel.basisCheck):
            self.otherBasis = insecureCommChannel.basisCheck.copy()
            insecureCommChannel.basisCheck.clear()

    #Compare sent and received basis
    def compareBasis(self):
        if len(self.otherBasis) == self.PHOTON_PULSE_SIZE and len(self.randomBasis) == self.PHOTON_PULSE_SIZE and len(self.recordedPolarizations) == self.PHOTON_PULSE_SIZE:
            i = 0
            count = 0
            while i < self.PHOTON_PULSE_SIZE:
                if self.randomBasis[i] == self.otherBasis[i]:
                    count += 1
                i += 1

    #Send basis to a qkCommChannel for a sender/Alice
    def sendBasis(self, insecureChannel, basisC):
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureChannel.basisCheck = basisC

    #Drops any polarizations where the sender and receiver basis differ'd
    def dropInvalidPolars(self):
        if len(self.otherBasis) == self.PHOTON_PULSE_SIZE and len(self.randomBasis) == self.PHOTON_PULSE_SIZE and len(self.recordedPolarizations) == self.PHOTON_PULSE_SIZE:
            i = 0
            max = self.PHOTON_PULSE_SIZE
            while i < max:
                if self.randomBasis[i] != self.otherBasis[i]:
                    self.randomBasis.pop(i)
                    self.otherBasis.pop(i)
                    self.recordedPolarizations.pop(i)
                    max -= 1
                else:
                    i += 1
        else:
            print("Error - Required Data Not Initialized.")

    #Analyzes the recorded polarizations to determine the shared key received from a sender through a channel.
    def setBitString(self):
        self.sharedKey.clear()
        if len(self.recordedPolarizations) <= self.PHOTON_PULSE_SIZE and len(self.recordedPolarizations) > 0:
            i = 0
            while i < len(self.recordedPolarizations):
                if self.recordedPolarizations[i] == 0:
                    self.sharedKey.append(0)
                elif self.recordedPolarizations[i] == 90:
                    self.sharedKey.append(1)
                elif self.recordedPolarizations[i] == 45:
                    self.sharedKey.append(0)
                elif self.recordedPolarizations[i] == 135:
                    self.sharedKey.append(1)
                i += 1

    #Sends a subBitString to a qkCommChannel, the sub key is just sharedKey[0->approx half]
    def sendSubBitString(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureCommChannel.subSharedKey.clear()
        if len(self.sharedKey) > 0:
            insecureCommChannel.subSharedKey = (self.sharedKey[0: (int((len(self.sharedKey))/2))]).copy()

    #Retrieves a subBitString from a qkCommChannel, this will be compared against the local unvalidated shared key
    def getSubBitString(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        self.subSharedKey.clear()
        if len(insecureCommChannel.subSharedKey) > 0:
            self.subSharedKey = insecureCommChannel.subSharedKey.copy()
            insecureCommChannel.subSharedKey.clear()
        else:
            print("Error - CommChannel's Sub Shared Key Is Empty!")

    #Decides if a sub shared key is valid enough, to validate a shared key
    def decide(self):
        if len(self.subSharedKey) > 0 and len(self.sharedKey)>len(self.subSharedKey):
            i = 0
            count = 0
            while i < len(self.subSharedKey):
                if self.subSharedKey[i] == self.sharedKey[i]:
                    count += 1
                i += 1
            if count >= self.MIN_REQ_OF_SHARED:
                self.decision = 1
            else:
                self.decision = 0
        else:
            self.decision = 0
            print("Error - decide() - otherSubSharedKey || sharedKey - Invalid")

    #Sends a decision to a qkCommChannel
    def sendDecision(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        if self.decision != -1:
            insecureCommChannel.decision = self.decision
        else:
            print("Error - sendDecision() - decision - Invalid")

    #Retrieves a decision value from a qkCommChannel
    def getDecision(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        if insecureCommChannel != -1:
            self.otherDecision = insecureCommChannel.decision
            if self.decision == 1 and self.otherDecision == 1:
                self.validKey = 1
            else:
                self.validKey = 0
        else:
            print("Error - sendDecision() - decision - Invalid")

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