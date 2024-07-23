from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    secret_target = SecretInteger(Input(name="secret_target", party=party_1))
    secret_guess = SecretInteger(Input(name="secret_guess", party=party_2))
    is_same_num = secret_target == secret_guess
    return [Output(is_same_num, "is_same_num", party=party_3)]