__author__ = 'Jakehp'
from random import randint
import qkPhoton
import qkCommChannel
import qkComm


#Receivers *cannot* access any photons - except via measurement
class qkReceiver(qkComm.qkComm):

    PHOTON_PULSE_SIZE = 128
    MIN_REQ_OF_SHARED = 25

    def __init__(self):
        self.photon_polars = []
        self.random_basis = []
        self.other_basis = []
        self.shared_key = []
        self.sub_shared_key = []
        self.decision = -1
        self.other_decision = -1
        self.valid_key = -1

    #Computes random basis's for random_basis list
    def set_random_basis(self):
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
        self.measure_polarizations(arg1)
        return

    #Measure and record all polarizations from photon pulse in the comm channel
    def measure_polarizations(self, insecure_comm_channel):
        assert isinstance(insecure_comm_channel, qkCommChannel.qkCommChannel), 'Invalid Arg'
        if len(insecure_comm_channel.photon_pulse) != self.PHOTON_PULSE_SIZE:
            print("CommChannel has no photons for receiver || CommChannel # of pulses != receivers photon_pulse_size")
            return -1
        self.set_random_basis()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            temp_pho = insecure_comm_channel.photon_pulse[i]
            assert isinstance(temp_pho, qkPhoton.qkPhoton), 'Not a qkPhoton object - Error'
            self.photon_polars.append(temp_pho.measure(self.random_basis[i]))
            i += 1
        insecure_comm_channel.photon_pulse.clear()
        return

    #Prints All Data
    def print_all(self):
        print("qkReceiver measured polars       ", self.photon_polars)
        print("qkReceiver Random Basis:         ", self.random_basis)
        print("Sender's Basis:                  ", self.other_basis)
        print("qkReceiver's shared_key:         ", self.shared_key)
        print("qkReceiver's sub_shared_key:     ", self.sub_shared_key)

    #Prints Lengths Of Data
    def print_details(self):
        print("Receiver's Photon Polarizations:  ", len(self.photon_polars))
        print("Receiver's Random Basis:          ", len(self.random_basis))
        print("Sender's Basis:                   ", len(self.other_basis))