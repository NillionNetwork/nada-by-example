from nada_dsl import *
import nada_numpy as na

def is_number_present_in_list(array: List[SecretInteger], value: Integer) -> SecretBoolean:
    result = Integer(0)
    for element in array:
        # If the element is equal to the value, add 1 to the result.
        result += (value == element).if_else(Integer(1), Integer(0))
    return (result > Integer(0))

def nada_main():
    num_parties = 10
    parties = na.parties(num_parties)

    secrets_list = []
    for i in range(num_parties):
        secrets_list.append(
            SecretInteger(Input(name="num_" + str(i), party=parties[i]))
        )

    # Check if 100 is present in one of the parties.
    is_present_1 = is_number_present_in_list(secrets_list, Integer(100))

    # Check if 99 is present in one of the parties.
    is_present_2 = is_number_present_in_list(secrets_list, Integer(99))

    return [
        Output(is_present_1, "is_present_1", party=parties[0]),
        Output(is_present_2, "is_present_2", party=parties[0]),
    ]
