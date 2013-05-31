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

    #Sending basis's to bob

Alice.sendBasisChecks(insecureChannel, Alice.basisCheck.copy())
Bob.checkSenderBasis(insecureChannel)
Bob.compareBasis()

    #Bob sends ACKS - and Alice retransmits if necessary.

#Bob.acknowledge(insecureChannel)
#Alice.checkForRetransmit(insecureChannel)

Alice.printAll()
insecureChannel.printAll()
Bob.printAll()
