from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    num_1 = SecretInteger(Input(name="num_1", party=party_alice))
    num_2 = SecretInteger(Input(name="num_2", party=party_bob))
    
    # Generate a secret integer with the random value in the range of 0 to max
    max = 10
    random_int = SecretInteger.random() % Integer(max+1)

    sum = num_1 + num_2
    check_min = (sum + random_int)  >= (Integer(0) + sum)
    check_max = (sum + random_int)  <= (Integer(max) + sum)
    return [
        Output(check_min, "check_min", party_charlie),
        Output(check_max, "check_max", party_charlie)
    ]