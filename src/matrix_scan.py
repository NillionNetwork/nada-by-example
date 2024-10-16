from nada_dsl import *
import nada_numpy as na

# Return the all coordinates where the value excists
def find_number_present_in_list(array: List[List[SecretInteger]], value: SecretInteger) -> List[List[Integer]]:
    result = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            coordinate = []
            # Get the coordinate[x, y].  If no match, set the coordinate to [-1, -1]
            x = (value == array[i][j]).if_else(Integer(i), Integer(-1))
            y = (value == array[i][j]).if_else(Integer(j), Integer(-1))
            result.append([x,  y])

    return result

def nada_main():
    num_row = 3
    row = na.parties(num_row)

    target_number = Party(name="target")
    target_number = SecretInteger(Input(name="target_number", party=target_number))

    # Create the matrix
    matrix: list[list[SecretInteger]] = []
    
    # Get the user inputs for the first row and add it to the matrix
    matrix_row_1 = []
    for i in range(num_row):
        matrix_row_1.append(
            SecretInteger(Input(name="row_0_" + str(i), party=row[i]))
        )
    matrix.append(matrix_row_1)

    # Get the user inputs for the second row and add it to the matrix
    matrix_row_2 = []
    for i in range(num_row):
        matrix_row_2.append(
            SecretInteger(Input(name="row_1_" + str(i), party=row[i]))
        )
    matrix.append(matrix_row_2)

    # Scan a matrix for a specific value
    value_excists = find_number_present_in_list(matrix, target_number)

    outputs = []

    for i in range(len(value_excists)):
        outputs.append(Output(value_excists[i][0], "value_excists_" + str(i) + "_x",  party=row[0]))
        outputs.append(Output(value_excists[i][1], "value_excists_" + str(i) + "_y",  party=row[0]))

    return outputs