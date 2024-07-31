from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    numerator = SecretInteger(Input(name="numerator", party=party_alice))
    denominator = SecretInteger(Input(name="denominator", party=party_bob))
    quotient = numerator / denominator
    return [Output(quotient, "quotient", party_charlie)]