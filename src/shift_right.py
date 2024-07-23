from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    base = SecretInteger(Input(name="base", party=party_1))
    shift = PublicUnsignedInteger(Input(name="shift", party=party_2))
    # right shift is the same as (base // 2^shift)
    # where // represents integer division discarding any remainder
    result = base >> shift
    return [Output(result, "right_shift_result", party=party_3)]