__author__ = 'Jakehp'
import qkCommChannel


    #Shared Functions:
    #-setBitString
    #-setSubBitString
    #-dropInvalidPolars
    #-getBasis
    #-sendBasis
    #-printAll
    #-printDetails
class qkComm(object):

    PHOTON_PULSE_SIZE = 128
    MIN_SHARED_REQ = 25

    def __init__(self):
        self.randomBasis = []
        self.otherBasis = []
        self.photonPolars = []
        self.sharedKey = []
        self.subSharedKey = []
        self.decision = -1
        self.otherDecision = -1
        self.validKey = -1

#BASIS STUFF
    #Retrieve sender basis's and check against local random basiss
    def checkOtherBasis(self, insecureCommChannel):
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

#POLAR STUFF
        #Drops any polarizations where the sender and receiver basis differ'd
    def dropInvalidPolars(self):
        if len(self.otherBasis) == self.PHOTON_PULSE_SIZE and len(self.randomBasis) == self.PHOTON_PULSE_SIZE and len(self.photonPulse) == self.PHOTON_PULSE_SIZE and len(self.photonPolars) == self.PHOTON_PULSE_SIZE:
            i = 0
            max = self.PHOTON_PULSE_SIZE
            while i < max:
                if self.randomBasis[i] != self.otherBasis[i]:
                    self.randomBasis.pop(i)
                    self.otherBasis.pop(i)
                    self.photonPolars.pop(i)
                    self.photonPulse.pop(i)
                    max -= 1
                else:
                    i += 1
        else:
            print("Error - Required Data Not Initialized.")

#BIT AND SUBBIT STRING STUFF
    #what happened here...
    #Analyzes the recorded polarizations to determine the shared key received from a sender through a channel.
    def setBitString(self):
        self.sharedKey.clear()
        if len(self.photonPolars) <= self.PHOTON_PULSE_SIZE and len(self.photonPolars) > 0:
            i = 0
            while i < len(self.photonPolars):
                if self.photonPolars[i] == 0:
                    self.sharedKey.append(0)
                elif self.photonPolars[i] == 90:
                    self.sharedKey.append(1)
                elif self.photonPolars[i] == 45:
                    self.sharedKey.append(0)
                elif self.photonPolars[i] == 135:
                    self.sharedKey.append(1)
                i += 1

    #Retrieve a subBitString from a qkCommChannel
    def getSubBitString(self, insecureChannel):
        self.subSharedKey.clear()
        assert isinstance(insecureChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        if len(insecureChannel.subSharedKey) > 0:
            self.subSharedKey = insecureChannel.subSharedKey.copy()
            insecureChannel.subSharedKey.clear()
        else:
            print("Error - qkCommChannel has no bit sub string.")

    #Sends a subBitString to a qkCommChannel, the sub key is just sharedKey[0->approx half]
    def sendSubBitString(self, insecureCommChannel):
        assert isinstance(insecureCommChannel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecureCommChannel.subSharedKey.clear()
        if len(self.sharedKey) > 0:
            insecureCommChannel.subSharedKey = (self.sharedKey[0: (int((len(self.sharedKey))/2))]).copy()

#DECISION STUFF
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

    #Decides if a sub shared key is valid enough, to validate a shared key
    def decide(self):
        if len(self.subSharedKey) > 0 and len(self.sharedKey) > len(self.subSharedKey):
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