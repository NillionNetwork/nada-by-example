from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    num_1 = SecretInteger(Input(name="num_1", party=party_alice))
    num_2 = SecretInteger(Input(name="num_2", party=party_bob))
    sum = num_1 + num_2

    # Debugging with print statements
    # Comment out or remove print statements before compiling Nada programs,
    # as compilation will fail if any print statements are included 👇

    # print(num_1) # SecretInteger(inner=Input(inner=None))
    # print(type(sum)) # <class 'nada_dsl.nada_types.types.SecretInteger'>
    # print(sum) # SecretInteger(inner=<nada_dsl.operations.Addition object at 0x104ba5e20>)
    return [Output(sum, "sum", party_charlie)]

# Include the print statements for debugging, then 
# run this program from the root with `python3 src/debug.py`
# to see printed values from the cli
if __name__ == "__main__":
    nada_main()