__author__ = 'Jakehp'


    #Shared Data:
    #-PHOTON_PULSE_SIZE
    #-randomBasis
    #-otherBasis
    #-photonPolars
    #-sharedKey
    #-subSharedKey
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
