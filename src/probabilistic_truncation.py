from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    base = SecretInteger(Input(name="base", party=party_alice))
    precision = PublicUnsignedInteger(Input(name="precision", party=party_bob))
    # reduce the precision of base with some randomness
    # precision determines the number of bits to retain
    result = base.trunc_pr(precision)
    return [Output(result, "trunc_pr_result", party=party_charlie)]