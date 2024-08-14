"""Implementation of the square root function using the Newton method
with n iterations - set to 41 by default."""

from nada_dsl import *
import time

n_iterations = 41
def nada_main():

    party1 = Party(name="Party1")

    num = SecretInteger(Input(name="num", party=party1))
    guess = num

    for _ in range(n_iterations):
        div1 = guess
        div2 = num / guess
        div2 = div2 / guess
        guess = Integer(2) * div1 +  div2
        guess = guess / Integer(3)
    return [Output(guess, "my_output", party1)]

if __name__ == "__main__":
   nada_main()
