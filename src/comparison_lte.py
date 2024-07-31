from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    x = SecretInteger(Input(name="x", party=party_alice))
    y = SecretInteger(Input(name="y", party=party_bob))
    # Comparison: x <= y (Less Than or Equal To)
    result = x <= y
    return [Output(result, "x_less_than_or_equal_y", party=party_charlie)]