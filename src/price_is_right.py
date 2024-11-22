from nada_dsl import *

def nada_main():
    price = Party(name="Price")
    player1 = Party(name="Player1")
    player2 = Party(name="Player2")

    right_price = SecretInteger(Input(name="Price", party=price))
    player1_input = SecretInteger(Input(name="Player1", party=player1))
    player2_input = SecretInteger(Input(name="Player2", party=player2))

    # calculate the difference between the guess and the price
    # set the value to -1 if the guess is greater than the price
    player1_close_value = (player1_input > right_price).if_else(Integer(-1), right_price - player1_input)
    player2_close_value = (player2_input > right_price).if_else(Integer(-1), right_price - player2_input)

    condition1 = player1_close_value < player2_close_value
    exceeding_condition1 = player1_close_value == Integer(-1)
    exceeding_condition2 = player2_close_value == Integer(-1)

    # check who guess that is closest to the actual price 
    result = condition1.if_else(Integer(1), Integer(2))

    # check who guess exceed the actual price
    result = exceeding_condition1.if_else(Integer(2), result)
    result = exceeding_condition2.if_else(Integer(1), result)

    # if all guesses exceed the actual price or if it a tie, return 0 for no winner
    result = (player1_close_value == player2_close_value).if_else(Integer(0), result)
    
    # O - no winner
    # 1 - player 1 win
    # 2 - player 2 win
    return [Output(result, "winner", price)]