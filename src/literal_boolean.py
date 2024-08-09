from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")

    # Start value for literal boolean
    is_sum_greater_than_five = Boolean(False)

    public_num_1 = PublicInteger(Input(name="public_num_1", party=party_alice))
    public_num_2 = PublicInteger(Input(name="public_num_2", party=party_bob))
    is_sum_greater_than_five =  (public_num_1 + public_num_2) > Integer(5)
    
    return [Output(is_sum_greater_than_five, "result", party_charlie)]