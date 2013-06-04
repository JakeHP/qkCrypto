__author__ = 'Jakehp'
import qkSender
import qkCommChannel
import qkReceiver

    #Amount of similar bits required to be considered a shared key

similar_bit_req = 50

    #Entity Creation

Alice = qkSender.qkSender()
insecureChannel = qkCommChannel.qkCommChannel()
Bob = qkReceiver.qkReceiver()
#Eve = qkAttacker.qkAttacker()

    #Creation, sending, attacking and receiving+measuring of photons

Alice.createPhotonPulse()

Alice.send(insecureChannel, Alice.photonPulse.copy())
#Eve.attack(insecureChannel)
Bob.measurePolarizations(insecureChannel)

    #Alice sends basis's

Alice.sendBasis(insecureChannel, Alice.randomBasis.copy())
Bob.checkSenderBasis(insecureChannel)
Bob.compareBasis()

    #Bob sends basis

Bob.sendBasis(insecureChannel, Bob.senderBasis.copy())
Alice.checkReceiverBasis(insecureChannel)

    #Alice and bob compare basis to see if a certain # of shared bits was reached.

#Alice.dropInvalidPhotons()
#Bob.dropInvalidPhotons()

    #Alice and Bob compare sub set of the bit string (photon polarizations -> bits)

#Alice.sendSubBitString(insecureChannel,)
#Bob.sendSubBitString(insecureChannel,)
#Alice.getSubBitString(insecureChannel,)
#Bob.getSubBitString(insecureChannel,)

    #Alice and Bob agree or disagree

#Alice.sendDecision(insecureChannel)
#Bob.sendDecision(insecureChannel)
#Alice.getDecision(insecureChannel)
#Bob.getDecision(insecureChannel)

    #Alice and Bob can now try again in a new channel or use the shared key based on the decision

Alice.printAll()
insecureChannel.printAll()
Bob.printAll()
