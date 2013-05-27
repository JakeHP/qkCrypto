__author__ = 'Jakehp'
import qkCommChannel
import qkPhoton


#Receivers *cannot* access any photons - except via measurement

class qkReceiver:

    def __init__(self):
        self.recordedPolarizations = []
        self.randomBasis = []

    #setRandomBasis

    #Measure and record all polarizations from photon pulse

    #receive alice/sender basis's, get all same basis, check for differences in polarization - if so % bit difference -> MITM has measured
