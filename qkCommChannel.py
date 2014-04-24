__author__ = 'Jakehp'


#Kind of a useless class, all data is passed through here, so an attacker has the ability to see what's going on
#send_pulseers, receivers, and attackers manage transmitting the data to and from qkCommChannel
class qkCommChannel:

    def __init__(self):
        self.photon_pulse = []
        self.basis_check = []
        self.sub_shared_key = []
        self.decision = -1

    def print_all(self):
        print("qkCommChannel photon_pulse:      ", self.photon_pulse)
        print("qkCommChannel basis_check:       ", self.basis_check)
        print("qkCommChannel sub shared key:       ", self.sub_shared_key)