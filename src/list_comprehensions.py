from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    
    # Inputs from each party
    secret1 = SecretInteger(Input(name="secret1", party=party_alice))
    secret2 = SecretInteger(Input(name="secret2", party=party_bob))
    secret3 = SecretInteger(Input(name="secret3", party=party_charlie))
    
    # List of secrets
    secrets_list = [secret1, secret2, secret3]
    
    # Use List Comprehensions to multiply each secret by multiplier
    multiplier = Integer(2)
    doubled_secrets = [secret * multiplier for secret in secrets_list]
    
    # Return the outputs to party_alice
    return [
        Output(doubled_secrets[i], "doubled_secret_" + str(i + 1), party_alice)
        for i in range(3)
    ]