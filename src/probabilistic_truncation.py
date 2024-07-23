from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    base = SecretInteger(Input(name="base", party=party_1))
    precision = PublicUnsignedInteger(Input(name="precision", party=party_2))
    # reduce the precision of base with some randomness
    # precision determines the number of bits to retain
    result = base.trunc_pr(precision)
    return [Output(result, "trunc_pr_result", party=party_3)]