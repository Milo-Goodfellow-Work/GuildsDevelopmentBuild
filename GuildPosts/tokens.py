#Non project imports
import random

#Project imports

#This Number generator is not designed to be incredibly secure
#It is designed to create invite links and therefore it's security
#Is not a priority
def NumberGenerator():
    InviteKeyGen = random.SystemRandom()
    InviteKey = InviteKeyGen.randint(0,10000000000)
    return InviteKey
