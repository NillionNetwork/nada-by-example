from nada_dsl import *

def check_value_at_position(position_value: SecretInteger, target_secret_value: Integer) -> Boolean:
    return position_value == target_secret_value

def nada_main():
    gamemaker = Party(name="gamemaker")
    # Look for this constant value
    target_secret_value = Integer(1)
    
    # Define the matrix of SecretIntegers held by the gamemaker
    size = 3
    matrix = [
        [SecretInteger(Input(name=f"board_r{i}_c{j}", party=gamemaker)) for j in range(size)]
        for i in range(size)
    ]
    
    # Initialize variables to store the position of the target value
    target_row = Integer(-1)
    target_col = Integer(-1)
    
    # Iterate through the matrix to find the position of the target value
    for i in range(size):
        for j in range(size):
            position_value = matrix[i][j]
            is_target = check_value_at_position(position_value, target_secret_value)
            target_row = is_target.if_else(Integer(i), target_row)
            target_col = is_target.if_else(Integer(j), target_col)
    
    # Return the position of the target value
    return [Output(target_row, "target_row", gamemaker), Output(target_col, "target_col", gamemaker)]