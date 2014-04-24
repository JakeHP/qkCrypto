__author__ = 'Jakehp'
from random import randint
#Diagonal Eigenstate    - 45* or 135*
#Rectilinear Eigenstate - 0* or 90*
#B     0    1
#R     |0    -90
#D     /45    \135


class qkPhoton:

    def __init__(self):

        self.random_bit = -1
        self.random_basis = ""
        self.polarization = -1

    #Sets a random bit
    def set_random_bit(self):
        self.random_bit = randint(0, 1)
        return self.random_bit

    #Sets a random basis
    #R = rectilinear
    #D = diagonal
    def set_random_basis(self):
        x = randint(0, 1)
        if x == 0:
            self.random_basis = "R"
            return "R"
        else:
            self.random_basis = "D"
            return "D"

    #Sets polarization
    #0 for failure, due to random bits or basis not being set
    #1 for success
    def set_polarization(self):
        if self.random_bit < 0 or (self.random_basis != "R" and self.random_basis != "D"):
                return -1
        elif self.random_basis == "R":
            if self.random_bit == 0:
                self.polarization = 0
                return 0
            elif self.random_bit == 1:
                self.polarization = 90
                return 90
        elif self.random_basis == "D":
            if self.random_bit == 0:
                self.polarization = 45
                return 45
            if self.random_bit == 1:
                self.polarization = 135
                return 135

    #Attempts to measure a photon based on a certain sender's basis
    #arg1 = the measuring basis
    #Returns a polarization
    def measure(self, arg1):
        if arg1 != "R" and arg1 != "D":
            return -1
        if arg1 == self.random_basis:
            return self.polarization
        else:
            if arg1 == "R":
                x = randint(0, 1)
                if x == 0:
                    self.polarization = 0
                    return 0
                else:
                    self.polarization = 90
                    return 90
            elif arg1 == "D":
                y = randint(0, 1)
                if y == 0:
                    self.polarization = 45
                    return 45
                else:
                    self.polarization = 135
                    return 135