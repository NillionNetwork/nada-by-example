from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    dividend = SecretInteger(Input(name="dividend", party=party_alice))
    divisor = SecretInteger(Input(name="divisor", party=party_bob))
    # modulo
    remainder = dividend % divisor 
    return [Output(remainder, "remainder", party_charlie)]