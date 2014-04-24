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
        self.recorded_polarizations = []
        self.random_basis = []
        self.other_basis = []
        self.shared_key = []
        self.sub_shared_key = []
        self.decision = -1
        self.other_decision = -1
        self.valid_key = -1

    #Computes random basis's for random_basis list
    def setrandom_basis(self):
        self.random_basis.clear()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            x = randint(0, 1)
            if x == 0:
                self.random_basis.append("R")
            else:
                self.random_basis.append("D")
            i += 1
        return

    #Simply exists for ease of understanding
    def receive(self, arg1):
        self.measurePolarizations(arg1)
        return

    #Measure and record all polarizations from photon pulse in the comm channel
    def measurePolarizations(self, insecure_comm_channel):
        assert isinstance(insecure_comm_channel, qkCommChannel.qkCommChannel), 'Invalid Arg'
        if len(insecure_comm_channel.photon_pulse) != self.PHOTON_PULSE_SIZE:
            print("CommChannel has no photons for receiver || CommChannel # of pulses != receivers photon_pulse_size")
            return -1
        self.setrandom_basis()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            tempPho = insecure_comm_channel.photon_pulse[i]
            assert isinstance(tempPho, qkPhoton.qkPhoton), 'Not a qkPhoton object - Error'
            self.recorded_polarizations.append(tempPho.measure(self.random_basis[i]))
            i += 1
        insecure_comm_channel.photon_pulse.clear()
        return

    #Prints All Data
    def printAll(self):
        print("qkReceiver recorded_polars:      ", self.recorded_polarizations)
        print("qkReceiver Random Basis:        ", self.random_basis)
        print("Sender's Basis:                 ", self.other_basis)
        print("qkReceiver's shared_key:         ", self.shared_key)
        print("qkReceiver's sub_shared_key:      ", self.sub_shared_key)

    #Prints Lengths Of Data
    def printDetails(self):
        print("qkSender Photon Polarizations:  ", len(self.recorded_polarizations))
        print("qkSender Random Basis:          ", len(self.random_basis))
        print("Receiver's Basis:               ", len(self.other_basis))