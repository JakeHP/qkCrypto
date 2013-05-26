__author__ = 'Jakehp'
from random import randint

#Diagonal Eigenstate    - 45* or 135*
#Rectilinear Eigenstate - 0* or 90*
#B     0    1
#R     |    -
#D     /    \

class qkPhoton:
    def __init__(self):
        self.randomBit = -1
        self.randomBasis = ""
        self.polarization = "~"

    #Sets a random bit
    def setRandomBit(self):
        self.randomBit=randint(0,1)
        return self.randomBit

    #Sets a random basis
    #R = rectilinear
    #D = diagonal
    def setRandomBasis(self):
        x = randint(0,1)
        if x == 0:
            self.randomBasis = "R"
            return "R"
        else:
            self.randomBasis = "D"
            return "D"

    #Sets polarization
    #0 for failure, due to random bits or basis not being set
    #1 for success
    def setPolarization(self):

        if self.randomBit < 0 or (self.randomBasis != "R" and self.randomBasis != "D"):
                return 0
        elif self.randomBasis == "R":
            if self.randomBit == 0:
                self.polarization = "|"
                return "|"
            elif self.randomBit == 1:
                self.polarization = "-"
                return "-"
        elif self.randomBasis == "D":
            if self.randomBit == 0:
                self.polarization = "/"
                return "/"
            if self.randomBit == 1:
                self.polarization="\\"
                return "\\"

    #Attempts to measure a photon based on a certain sending basis
    #arg1 = the measuring basis
    #Returns a polarization
    def measure(self, arg1):
        if arg1 != "R" and arg1 != "D":
            return 0
        if arg1 == self.randomBasis:
            return self.polarization
        else:
            if arg1 == "R":
                x = randint(0,1)
                if x == 0:
                    self.polarization("|")
                    return "|"
                else:
                    self.polarization("-")
                    return "-"
            elif arg1 == "D":
                x = randint(0,1)
                if x == 0:
                    self.polarization = "/"
                    return "/"
                else:
                    self.polarization = "\\"
                    return "\\"