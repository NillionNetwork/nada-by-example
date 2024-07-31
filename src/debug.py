from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    num_1 = SecretInteger(Input(name="num_1", party=party_alice))
    num_2 = SecretInteger(Input(name="num_2", party=party_bob))
    sum = num_1 + num_2
    # Nada DSL does not currently support print statements and will fail if any are included
    # instead of print(), debug by raising an exception
    # uncomment any one of the raise Exception() lines
    # then build this program with `nada build debug` to print the inside to the terminal
    
    # raise Exception(type(sum)) 
    # raise Exception(sum) 
    # raise Exception(party_alice) 
    
    return [Output(sum, "sum", party_charlie)]