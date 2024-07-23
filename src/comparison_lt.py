from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    x = SecretInteger(Input(name="x", party=party_1))
    y = SecretInteger(Input(name="y", party=party_2))
    # Comparison: x < y (Less Than)
    result = x < y
    return [Output(result, "x_less_than_y", party=party_3)]