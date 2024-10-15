from nada_dsl import *
import nada_numpy as na

size = 5

def nada_main():
    
    party_alice = Party(name="Party_Alice")
    parties = na.parties(size)
    n = SecretInteger(Input(name="n", party=party_alice))

    
    list = [SecretInteger(Input(name=f"num_{i}", party=parties[i])) for i in range(size)]
    
    
    total_size = Integer(size)
    element_3 = Integer(1)

    element = Integer(0)
    index = total_size - n
    for i in range(size):
        number = Integer(i)
        element += (number == index).if_else(list[i], Integer(0))

    return [Output(element, "nth_element", party_alice)]
