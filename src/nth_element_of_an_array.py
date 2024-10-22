from nada_dsl import *
import nada_numpy as na

size = 5

def nada_main():
    """
    This function selects the n-th element from a list of secret integers. 
    The value of 'n' is provided to specify the index of the element required
    """
    
    party_alice = Party(name="Party_Alice")
    parties = na.parties(size)
    n = SecretInteger(Input(name="n", party=party_alice))
    list = [SecretInteger(Input(name=f"num_{i}", party=parties[i])) for i in range(size)]

    element = Integer(0)
    for i in range(size):
        element += (Integer(i) == n-Integer(1)).if_else(list[i], Integer(0))

    return [Output(element, "nth_element", party_alice)]

