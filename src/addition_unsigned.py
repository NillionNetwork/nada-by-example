from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    num_1 = SecretUnsignedInteger(Input(name="num_1", party=party_alice))
    num_2 = SecretUnsignedInteger(Input(name="num_2", party=party_bob))
    sum = num_1 + num_2
    return [Output(sum, "sum", party_charlie)]