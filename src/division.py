from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    numerator = SecretInteger(Input(name="numerator", party=party_1))
    denominator = SecretInteger(Input(name="denominator", party=party_2))
    quotient = numerator / denominator
    return [Output(quotient, "quotient", party_3)]