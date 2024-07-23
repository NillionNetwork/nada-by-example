from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    party_2 = Party(name="Bob")
    party_3 = Party(name="Charlie")
    dividend = SecretInteger(Input(name="dividend", party=party_1))
    divisor = SecretInteger(Input(name="divisor", party=party_2))
    # modulo
    remainder = dividend % divisor 
    return [Output(remainder, "remainder", party_3)]