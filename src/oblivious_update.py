from nada_dsl import *
import nada_numpy as na

### Updates the elements of the list which matches the old_value to a new_value
def nada_main():
    party_alice = Party(name="Party_Alice")
    party_bob = Party(name="Party_Bob")

    # Getting the old and new value to update the list
    old_value = SecretInteger(Input(name="old_value", party=party_alice))
    new_value = SecretInteger(Input(name="new_value", party=party_bob))

    size_of_list = 5
    parties = na.parties(size_of_list)

    # Get the values of the list
    secrets_list = []
    for i in range(size_of_list):
        secrets_list.append(
            SecretInteger(Input(name="num_" + str(i), party=parties[i]))
        )
    
    # Update the list
    for i in range(size_of_list):
        secrets_list[i] = (secrets_list[i] == old_value).if_else(new_value, secrets_list[i])

    return [
        Output(secrets_list[i], "modified_num_" + str(i + 1), party=parties[i])
        for i in range(size_of_list)
    ]

