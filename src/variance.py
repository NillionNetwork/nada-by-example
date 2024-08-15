from nada_dsl import *
import nada_numpy as na

DIM = 10

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
    return  var

def nada_main():
    party1 = Party(name="Party1")

    arr = na.array([DIM], party1, "array", SecretInteger)

    var = variance(arr)

    return na.output(var, party1, "variance")
