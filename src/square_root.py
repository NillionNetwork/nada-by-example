"""Implementation of the square root function using the Newton method
with n iterations - set to 12 by default"""

from nada_dsl import *

n_iterations = 12
def nada_main():

    party1 = Party(name="Party1")

    num = SecretInteger(Input(name="num", party=party1))
    guess = num

    for _ in range(n_iterations):
        guess = (guess + num / guess) / Integer(2)

    return [Output(guess, "my_output", party1)]