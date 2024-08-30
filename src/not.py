from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    
    secret_target = SecretInteger(Input(name="secret_target", party=party_alice))
    secret_guess = SecretInteger(Input(name="secret_guess", party=party_bob))
    
    # equal to check (==)
    check_is_equal_to = secret_target == secret_guess
    
    # the not operator (~) is used to invert or negate a boolean value
    check_is_not_equal_to = ~check_is_equal_to

    return [
        Output(check_is_not_equal_to, "check_is_not_equal_to", party_charlie),
    ]