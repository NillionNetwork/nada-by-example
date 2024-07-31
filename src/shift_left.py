from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    base = SecretInteger(Input(name="base", party=party_alice))
    shift = PublicUnsignedInteger(Input(name="shift", party=party_bob))
    # left shift is the same as (base * 2^shift)
    result = base << shift
    return [Output(result, "left_shift_result", party=party_charlie)]