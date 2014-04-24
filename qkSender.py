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

    def create_photon_pulse(self):
        self.photon_pulse.clear()
        self.random_basis.clear()
        i = 0
        while i < self.PHOTON_PULSE_SIZE:
            self.photon_pulse.append(self.create_photon())
            i += 1

    def create_photon(self):
        data = qkPhoton.qkPhoton()
        data.set_random_bit()
        basis = data.set_random_basis()
        self.random_basis.append(basis)
        polar = data.set_polarization()
        self.photon_polars.append(polar)
        return data

    #send_pulse a photon pulse
    def send_pulse(self, insecure_channel, p_pulse):
        assert isinstance(insecure_channel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecure_channel.photon_pulse = p_pulse

    #send_pulse a basis to a specified qkCommChannel
    def send_pulse_basis(self, insecure_channel, basis_c):
        assert isinstance(insecure_channel, qkCommChannel.qkCommChannel), 'Invalid Arg1'
        insecure_channel.basis_check = basis_c

    #Prints All Data
    def print_all(self):
        print("Sender's Photon Pulse:          ", self.photon_pulse)
        print("Sender's Photon Polarizations:  ", self.photon_polars)
        print("Sender's Basis:                 ", self.random_basis)
        print("Receiver's Basis:               ", self.other_basis)
        print("Sender's shared_key:            ", self.shared_key)
        print("Sender's sub shared_key:        ", self.sub_shared_key)

    #Prints Lengths Of Data
    def print_details(self):
        print("Sender's Photon Pulse:          ", len(self.photon_pulse))
        print("Sender's Photon Polarizations:  ", len(self.photon_polars))
        print("Sender's Random Basis:          ", len(self.random_basis))
        print("Receiver's Basis:               ", len(self.other_basis))

    def compare_two_arrays(self, arg1, arg2):
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