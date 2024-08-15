from nada_dsl import *
import nada_numpy as na

DIM = 10

def argmax(array: na.NadaArray, index_party: Party):
    # The result (the index of the argmax)
    result = Integer(-1)

    # The current index of the loop. It is set to be a public value
    current_index = Integer(0)

    # Assume the max value is at index 0
    max_val = array[0]

    # Compare the remaining content of the array with max_val
    for v in array:
        # Is the current value, v, greater than max_val?
        cond = v >= max_val
        # If true, then max_val is set to be v. Otherwise, it is not changed.
        max_val = cond.if_else(v, max_val)
        # If true, then result index is updated to the current index. Otherwise, it is not changed.
        result = cond.if_else(current_index, result)
        # Increment the index counter.
        current_index = current_index + Integer(1)
    return result


def nada_main():
    party1 = Party(name="Party1")
    # A party to keep track of the index of the result
    index_party = Party(name="index_party")

    array = na.array([DIM], party1, "array", SecretInteger)

    result = argmax(array, index_party)

    return na.output(result, index_party, "argmax")

if __name__ == "__main__":
   nada_main()

