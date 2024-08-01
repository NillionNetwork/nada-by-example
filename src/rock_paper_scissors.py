from nada_dsl import *

def nada_main():
    player_1 = Party(name="Player_1") 
    player_2 = Party(name="Player_2")

    # Possible play choices
    # 0 - Rock
    # 1 - Paper
    # 2 - Scissors 
    choice_player_1 = SecretInteger(Input(name="choice_player_1", party=player_1))
    choice_player_2 = SecretInteger(Input(name="choice_player_2", party=player_2))

    # modular arithmetic, cyclical RPS logic
    result = (choice_player_1 - choice_player_2) % Integer(3)

    # Which player won?
    # 0 - Tie
    # 1 - Player 1 won
    # 2 - Player 2 won
    winner = (
        (result > Integer(0)).if_else(
            (result > Integer(1)).if_else(Integer(2), Integer(1)),
            Integer(0)
        )
    )

    out = Output(winner, "winning_player_number", player_1)

    return [out]