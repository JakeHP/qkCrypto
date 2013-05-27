__author__ = 'Jakehp'
import qkSender
import qkCommChannel
import qkReceiver

#Entity Creation
Alice = qkSender.qkSender()
insecureChannel = qkCommChannel.qkCommChannel()
Bob = qkReceiver.qkReceiver()

#Creation, sending, attacking and receiving of photons
Alice.createPhotonPulse()
Alice.send(insecureChannel, Alice.photonPulse)
#Bob.receive(insecureChannel)

#Sending basis's to bob
Alice.sendBasisChecks(insecureChannel, Alice.basisCheck)

insecureChannel.printAll()

