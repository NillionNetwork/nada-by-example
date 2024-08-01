from nada_dsl import *
import nada_numpy as na

def add(left: SecretInteger, right: SecretInteger) -> SecretInteger:
    return left + right

def reduce(array: List[SecretInteger], fn: nada_fn, initialValue: Integer) -> SecretInteger:
    total = Integer(initialValue)
    for element in array:
        total = fn(total, element)
    return total

def nada_main():
    num_parties = 10
    parties = na.parties(num_parties)

    secrets_list = []
    for i in range(num_parties):
        secrets_list.append(
            SecretInteger(Input(name="num_" + str(i), party=parties[i]))
        )
    total = reduce(secrets_list, add, 0)

    return [Output(total, "total", party=parties[0])]