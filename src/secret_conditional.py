from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    
    # Alice inputs a secret boolean that determines whether or not to double Bob's secret input
    should_double = SecretBoolean(Input(name="should_double", party=party_alice))
    secret_num = SecretInteger(Input(name="secret_num", party=party_bob))

    result = should_double.if_else(secret_num * Integer(2), secret_num)

    # Charlie receives the result, but doesn't know
    # whether Bob's original input has doubled
    return [Output(result, "result", party_charlie)]