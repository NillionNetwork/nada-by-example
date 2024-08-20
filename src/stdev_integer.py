from nada_dsl import *
import nada_numpy as na

DIM = 10  # Array dimension


def mean(array: na.NadaArray):
    sum = Integer(0)

    # Compute the sum
    for v in array:
        sum += v

    # Divide the sum by the number of the elements
    m = sum / Integer(DIM)
    return m


def variance(array: na.NadaArray):
    # Compute the mean
    m = mean(array)

    # Initialize the sum to 0
    sum = Integer(0)

    # Compute (x_i - mean)^2
    for v in array:
        diff = v - m
        sum += (diff * diff)

    var = sum / Integer(DIM)
    return var


# Computing the square root - https://github.com/NillionNetwork/nada-by-example/blob/main/src/square_root.py
def sqrt(num: SecretInteger, n_iterations=12):
    guess = num

    for _ in range(n_iterations):
        guess = (guess + num / guess) / Integer(2)

    return guess


def stdev(array: na.NadaArray):
    # Compute the variance
    var = variance(array)
    # STD = sqrt(variance)
    std = sqrt(var)
    # Return the result
    return std


def nada_main():
    party1 = Party(name="Party1")

    arr = na.array([DIM], party1, "array", SecretInteger)

    std = stdev(arr)

    return na.output(std, party1, "stdev_integer")
