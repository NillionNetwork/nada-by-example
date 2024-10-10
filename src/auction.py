from nada_dsl import *

def nada_main():
    # Define parties
    auctioneer = Party(name="auctioneer")
    parties = [Party(name=f"Party{i}") for i in range(5)]
    
    # Collect bids from each party
    bids = [SecretInteger(Input(name=f"bid_{i}", party=parties[i])) for i in range(5)]
    
    # Initialize variables to track the highest bid and the winning party index
    highest_bid = bids[0]
    winning_index = Integer(0)
    
    # Compare bids to find the highest
    for i in range(1, 5):
        is_higher = bids[i] > highest_bid
        highest_bid = is_higher.if_else(bids[i], highest_bid)
        winning_index = is_higher.if_else(Integer(i), winning_index)
    
    # Output the highest bid and the winning party index
    return [
        Output(highest_bid, "highest_bid", auctioneer),
        Output(winning_index, "winning_index", auctioneer)
    ]
