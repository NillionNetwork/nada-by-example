from nada_dsl import *

def nada_main():
    party = Party(name="Alice")
    num = SecretInteger(Input(name="favorite_number", party=party))
    base = num.reveal()
    # power operations can only be performed on public integers, so the input needs to be revealed
    num_squared = base ** Integer(2)
    return [Output(num_squared, "num_squared", party)]