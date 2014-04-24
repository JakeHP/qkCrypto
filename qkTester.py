__author__ = 'Jakehp'
import qkSender
import qkCommChannel
import qkReceiver

    #Entity Creation

Alice = qkSender.qkSender()
insecure_channel = qkCommChannel.qkCommChannel()
Bob = qkReceiver.qkReceiver()
#Eve = qkAttacker.qkAttacker()

    #Creation, sending, attacking and receiving+measuring of photons

Alice.createphoton_pulse()

Alice.send(insecure_channel, Alice.photon_pulse.copy())
#Eve.attack(insecure_channel)
Bob.measurePolarizations(insecure_channel)

    #Alice sends basis's

Alice.send_basis(insecure_channel, Alice.random_basis.copy())
Bob.checkother_basis(insecure_channel)
Bob.compareBasis()

    #Bob sends basis

Bob.send_basis(insecure_channel, Bob.random_basis.copy())
Alice.checkother_basis(insecure_channel)

    #Alice and bob compare basis to see if a certain # of shared bits was reached.

Alice.drop_invalid_polars()
Bob.drop_invalid_polars()

    #Alice and Bob both break their polarizations down into bitstrings/shared_key

Alice.set_bit_string()
Bob.set_bit_string()

    #Alice and Bob compare sub set of the bit string (photon polarizations -> bits)

Alice.send_sub_bit_string(insecure_channel)
Bob.get_sub_bit_string(insecure_channel)
Bob.send_sub_bit_string(insecure_channel)
Alice.get_sub_bit_string(insecure_channel)

    #Alice and Bob decide if each others sub shared keys are "equal" enough to trust the channel and declare a shared key

Alice.decide()
Bob.decide()

    #Alice and Bob send there decisions on whether the shared key is valid, by sending the decision to each other

Alice.send_decision(insecure_channel)
Bob.get_decision(insecure_channel)
Bob.send_decision(insecure_channel)
Alice.get_decision(insecure_channel)

    #Alice and Bob can now try again in a new channel or use the shared key based on the decision

if Alice.valid_key == 1 and Bob.valid_key == 1:
    if Alice.shared_key == Bob.shared_key:
        print("Alice & Bob's Shared Secret Key: ", Alice.shared_key)
        print("Length Of Shared Secret Key:     ", len(Alice.shared_key))
    else:
        print("Error in implementation (if no attacker set/req # of sub shared reached)")
else:
    print("Alice & Bob have not agreed upon a Shared Secret Key")