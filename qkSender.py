__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton
import qkComm


#will extend qkComm in the future
class qkSender(qkComm.qkComm):

    def __init__(self):
        self.photon_pulse = []
        self.random_basis = []
        self.other_basis = []
        self.photon_polars = []
        self.shared_key = []
        self.sub_shared_key = []
        self.decision = -1
        self.other_decision = -1
        self.valid_key = -1

    def createphoton_pulse(self):
        self.photon_pulse.clear()
        self.random_basis.clear()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            self.photon_pulse.append(self.createPhoton())
            i += 1

    def createPhoton(self):
        data = qkPhoton.qkPhoton()
        data.setRandomBit()
        basis = data.setrandom_basis()
        self.random_basis.append(basis)
        polar = data.setPolarization()
        self.photon_polars.append(polar)
        return data

    #Send a photon pulse
    def send(self, insecure_channel, pPulse):
        assert isinstance(insecure_channel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecure_channel.photon_pulse = pPulse

    #Send a basis to a specified qkCommChannel
    def send_basis(self, insecure_channel, basisC):
        assert isinstance(insecure_channel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecure_channel.basis_check = basisC

    #Prints All Data
    def printAll(self):
        print("qkSender Photon Pulse:          ", self.photon_pulse)
        print("qkSender Photon Polarizations:  ", self.photon_polars)
        print("qkSender Basis:                 ", self.random_basis)
        print("Receiver's Basis:               ", self.other_basis)
        print("qkSender's shared_key:           ", self.shared_key)
        print("qkSender's shared_key:           ", self.sub_shared_key)

    #Prints Lengths Of Data
    def printDetails(self):
        print("qkSender Photon Pulse:          ", len(self.photon_pulse))
        print("qkSender Photon Polarizations:  ", len(self.photon_polars))
        print("qkSender Random Basis:          ", len(self.random_basis))
        print("Receiver's Basis:               ", len(self.other_basis))

    def compareTwoArrays(self, arg1, arg2):
        test = 0
        if len(arg1) != len(arg2):
            print("Two Arrays - Not Equal!")
        else:
            i = 0
            while i < len(arg1):
                if arg1[i] != arg2[i]:
                    test = 1
                i += 1
            if test == 0:
                print("Two Arrays - Equal!")
            else:
                print("Two Arrays - Not Equal!")