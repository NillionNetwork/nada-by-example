from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    base = PublicInteger(Input(name="base", party=party_1))
    exponent = PublicInteger(Input(name="exponent", party=party_2))
    power = base ** exponent
    return [Output(power, "power", party_3)]