from nada_dsl import *
import nada_numpy as na

DIM = 10

# A party to keep track of the index of the result
index_party = Party(name="index_party")

# A party holding the public value of 1, used for addition
one_party = Party(name="one_party")

# The result (the index of the argmax)
result = SecretInteger(Input(name="indx", party=index_party))

# The current index of the loop. It is set to be a public value
current_indx = Integer(0)

# A public value of 1
one = Integer(1)

def argmax(array: na.NadaArray):
    global result, current_indx, one

    # Assume the max value is at index 0
    max_val = array[0]

    # Compare the remaining content of the array with max_val
    for v in array:
        # Is the current value, v, greater than max_val?
        cond = v > max_val
        # If true, then max_val is set to be v. Otherwise, it is not changed.
        max_val = cond.if_else(v, max_val)
        # If true, then result index is updated to the current index. Otherwise, it is not changed.
        result = cond.if_else(current_indx, result)
        # Increment the index counter.
        current_indx = current_indx + one
    return result


def nada_main():
    party1 = Party(name="Party1")

    array = na.array([DIM], party1, "array", SecretInteger)

    result = argmax(array)

    return na.output(result, index_party, "argmax")

if __name__ == "__main__":
   nada_main()