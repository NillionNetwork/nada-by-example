from nada_dsl import SecretInteger

import nada_numpy as na
from nada_numpy import shuffle


def nada_main():

    # Note:
    # The current shuffle operation only supports vectors with
    # a power-of-two size, e.g., 2, 4, 8, 16, 32, ... 
    size=4

    parties = na.parties(2)
    nums = na.array([size], parties[0], "num", SecretInteger)

    shuffled_nums = shuffle(nums)

    return (
        na.output(shuffled_nums, parties[1], "shuffled_num")
    )