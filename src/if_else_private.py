from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    
    conditional_num_1 = SecretInteger(Input(name="conditional_num_1", party=party_1))
    conditional_num_2 = SecretInteger(Input(name="conditional_num_2", party=party_2))

    secret_1 = SecretInteger(Input(name="secret_1", party=party_1))
    secret_2 = SecretInteger(Input(name="secret_2", party=party_2))
    
    # Private condition
    condition = conditional_num_1 > conditional_num_2
    conditional_product = condition.if_else(secret_1, secret_2) * Integer(2)
    
    return [Output(conditional_product, "conditional_product", party_3)]