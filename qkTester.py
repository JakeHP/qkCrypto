__author__ = 'Jakehp'
import qkPhoton

#quick test of photon creation, and measurement
p = qkPhoton.qkPhoton()
bit = p.setRandomBit()
basis = p.setRandomBasis()
polarization = p.setPolarization()

print (bit, basis, polarization)

pol = p.measure("R")

print ("measured pol: ", pol)