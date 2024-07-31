from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    base = PublicInteger(Input(name="base", party=party_alice))
    exponent = PublicInteger(Input(name="exponent", party=party_bob))
    power = base ** exponent
    return [Output(power, "power", party_charlie)]