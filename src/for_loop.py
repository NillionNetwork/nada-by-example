from nada_dsl import *

def nada_main():
    party_1 = Party(name="Alice")
    start_int = SecretInteger(Input(name="start", party=party_1))
    list_length = 3
    
    ascending_list = []
    for i in range(list_length):
        ascending_list.append(start_int + Integer(i))
    
    # Return outputs using a for loop
    outputs = []
    for i in range(len(ascending_list)):
        outputs.append(Output(ascending_list[i], "ascending_list_" + str(i), party_1))
    
    return outputs