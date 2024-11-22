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

    # Return the sum to party_alice
    return [Output(sum(secrets_list), "sum_list", party_alice) for i in range(3)]
