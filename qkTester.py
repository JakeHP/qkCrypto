__author__ = 'jake'
import qkPhoton

p = qkPhoton.qkPhoton()
bit = p.setRandomBit()
basis = p.setRandomBasis()
polarization = p.setPolarization()

print (bit, basis, polarization)