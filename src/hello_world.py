from nada_dsl import *

def nada_main():
    party = Party(name="Alice")
    num = SecretInteger(Input(name="favorite_number", party=party))
    return [Output(num, "output", party)]