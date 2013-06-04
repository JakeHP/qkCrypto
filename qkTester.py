__author__ = 'Jakehp'
import qkSender
import qkCommChannel
import qkReceiver

    #Entity Creation

Alice = qkSender.qkSender()
insecureChannel = qkCommChannel.qkCommChannel()
Bob = qkReceiver.qkReceiver()
#Eve = qkAttacker.qkAttacker()

    #Creation, sending, attacking and receiving of photons

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

    #Alice and bob compare basis to see if a certain # of shared bits was reached. 50

Alice.printAll()
insecureChannel.printAll()
Bob.printAll()
