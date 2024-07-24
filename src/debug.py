from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    num_1 = SecretInteger(Input(name="num_1", party=party_1))
    num_2 = SecretInteger(Input(name="num_2", party=party_2))
    sum = num_1 + num_2
    # Nada DSL does not currently support print statements and will fail if any are included
    # instead of print(), debug by raising an exception
    # uncomment any one of the raise Exception() lines
    # then build this program with `nada build debug` to print the inside to the terminal
    
    # raise Exception(type(sum)) 
    # raise Exception(sum) 
    # raise Exception(party_1) 
    
    return [Output(sum, "sum", party_3)]