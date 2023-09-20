import random
def generateRandomHash():
    return str("%032x" % random.getrandbits(128)) 

