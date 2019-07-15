#Non project imports
import random

#This Number generator is not designed to be incredibly secure
#It is designed to create invite links and therefore it's security
#Is not a priority (\_(0-0)_/)
def NumberGenerator():
    InviteKeyGen = random.SystemRandom()
    InviteKey = InviteKeyGen.randint(0,1000000)
    return InviteKey
