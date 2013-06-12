__author__ = 'Jakehp'
import qkSender
import qkCommChannel
import qkReceiver

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

Bob.sendBasis(insecureChannel, Bob.randomBasis.copy())
Alice.checkReceiverBasis(insecureChannel)

    #Alice and bob compare basis to see if a certain # of shared bits was reached.

Alice.dropInvalidPolars()
Bob.dropInvalidPolars()

    #Alice and Bob both break their polarizations down into bitstrings/sharedkey

Alice.setBitString()
Bob.setBitString()

    #Alice and Bob compare sub set of the bit string (photon polarizations -> bits)

Alice.sendSubBitString(insecureChannel)
Bob.getSubBitString(insecureChannel)
Bob.sendSubBitString(insecureChannel)
Alice.getSubBitString(insecureChannel)

    #Alice and Bob decide if each others sub shared keys are "equal" enough to trust the channel and declare a shared key

Alice.decide()
Bob.decide()

    #Alice and Bob send there decisions on whether the shared key is valid, by sending the decision to each other

Alice.sendDecision(insecureChannel)
Bob.getDecision(insecureChannel)
Bob.sendDecision(insecureChannel)
Alice.getDecision(insecureChannel)

    #Alice and Bob can now try again in a new channel or use the shared key based on the decision

if Alice.validKey == 1 and Bob.validKey == 1:
    if Alice.sharedKey == Bob.sharedKey:
        print("Alice & Bob's Shared Secret Key: ", Alice.sharedKey)
        print("Length Of Shared Secret Key:     ", len(Alice.sharedKey))
    else:
        print("Error in implementation (if no attacker set/req # of sub shared reached)")
else:
    print("Alice & Bob have not agreed upon a Shared Secret Key")