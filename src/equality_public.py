from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    secret_target = SecretInteger(Input(name="secret_target", party=party_alice))
    secret_guess = SecretInteger(Input(name="secret_guess", party=party_bob))
    is_same_num = secret_target.public_equals(secret_guess)
    return [Output(is_same_num, "is_same_num", party=party_charlie)]