from nada_dsl import *

def nada_main():
    party_weatherman = Party(name="Weather Man")
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    
    # The Weather Man inputs a public boolean
    is_raining = PublicBoolean(Input(name="is_raining", party=party_weatherman))

    num_1 = SecretInteger(Input(name="num_1", party=party_alice))
    num_2 = SecretInteger(Input(name="num_2", party=party_bob))
    sum = num_1 + num_2

    # If is raining is true, add 1 to the sum
    result = is_raining.if_else(sum + Integer(1), sum)

    # Charlie receives the result, but doesn't know
    # whether Bob's original input has doubled
    return [Output(result, "result", party_charlie)]