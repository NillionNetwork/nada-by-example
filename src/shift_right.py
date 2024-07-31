from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    base = SecretInteger(Input(name="base", party=party_alice))
    shift = PublicUnsignedInteger(Input(name="shift", party=party_bob))
    # right shift is the same as (base // 2^shift)
    # where // represents integer division discarding any remainder
    result = base >> shift
    return [Output(result, "right_shift_result", party=party_charlie)]