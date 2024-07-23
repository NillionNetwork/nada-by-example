from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    num_1 = SecretInteger(Input(name="num_1", party=party_1))
    num_2 = SecretInteger(Input(name="num_2", party=party_2))
    product = num_1 * num_2
    return [Output(product, "product", party_3)]