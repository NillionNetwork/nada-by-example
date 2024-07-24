from nada_dsl import *

def nada_main():
    gamemaker = Party(name="gamemaker")
    guesser = Party(name="guesser")
    ## workaround value
    public_integer_current_row_iterator = PublicInteger(Input(name="public_integer_current_row_iterator", party=gamemaker))
    public_integer_current_col_iterator = PublicInteger(Input(name="public_integer_current_col_iterator", party=gamemaker))

    # position (row and column in matrix) to guess
    guess_position_row = SecretInteger(Input(name="guess_position_row", party=guesser))
    guess_position_col = SecretInteger(Input(name="guess_position_col", party=guesser))

    # value to guess
    guess_secret_value = SecretInteger(Input(name="guess_secret_value", party=guesser))
    
    # define the matrix of SecretIntegers held by the gamemaker
    row_size = 3
    col_size = 5
    matrix = [
        [SecretInteger(Input(name=f"board_r{r}_c{c}", party=gamemaker)) for c in range(col_size)]
        for r in range(row_size)
    ]
    
    # Initialize variables to store the position of the target value
    found_row = Integer(-1)
    found_col = Integer(-1)
    found_int_value = Integer(-1)
    guesser_was_correct = Integer(-1)
    
    # Iterate through the matrix to find the secret guessed position to check 
    for r in range(row_size):
        current_row = public_integer_current_row_iterator
        for c in range(col_size):
            current_col = public_integer_current_col_iterator

            # secret booleans
            is_guesser_row = current_row == guess_position_row
            is_guesser_col = current_col == guess_position_col

            found_row = is_guesser_row.if_else(current_row, found_row)
            found_col = is_guesser_col.if_else(current_col, found_col)

            is_guesser_position = is_guesser_row.if_else(
                is_guesser_col.if_else(Integer(1), Integer(0))
                , Integer(0))
            
            is_guesser_position_boolean = is_guesser_position == Integer(1)
            current_secret_value = matrix[r][c]
            is_match = current_secret_value == guess_secret_value
            
            # if at the secret guesser position and the value is the same as the guessed value
            guessed_correctly_this_turn = is_guesser_position_boolean.if_else(
                is_match.if_else(Integer(1), Integer(0))
                , Integer(0))
            
            guesser_was_correct = (guessed_correctly_this_turn == Integer(1)).if_else(Integer(1), guesser_was_correct)
            
            found_int_value = (guessed_correctly_this_turn == Integer(1)).if_else(guess_secret_value, found_int_value)

            public_integer_current_col_iterator = public_integer_current_col_iterator + Integer(1)
        public_integer_current_col_iterator = public_integer_current_col_iterator - Integer(col_size)
        public_integer_current_row_iterator = public_integer_current_row_iterator + Integer(1)

    return [
        Output(found_row, "found_row", guesser), 
        Output(found_col, "found_col", guesser), 
        Output(found_int_value, "found_int_value", guesser), 
        Output(guesser_was_correct == Integer(1), "guesser_was_correct", gamemaker),
        Output(guesser_was_correct == Integer(1), "guesser_was_correct", guesser),
    ]