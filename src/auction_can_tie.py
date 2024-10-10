from nada_dsl import *

def nada_main():
    # Define the auctioneer as the party responsible for overseeing the auction results
    auctioneer = Party(name="auctioneer")
    
    # Create a list of 5 bidders participating in the auction, 'bidder_0' to 'bidder_4'
    bidders = [Party(name=f"bidder_{i}") for i in range(5)]
    
    # Collect bids from each bidder, where each bid is a SecretInteger input unique to the respective bidder
    bids = [SecretInteger(Input(name=f"bid_{i}", party=bidders[i])) for i in range(5)]
    
    # Determine the highest bid among all the bidders
    # Start by initializing the highest bid to the first bidder's bid
    highest_bid = bids[0]
    # Iterate through the remaining bids to update the highest bid if a higher one is found
    for i in range(1, 5):
        is_higher = bids[i] > highest_bid
        highest_bid = is_higher.if_else(bids[i], highest_bid)

    # Create a list of outputs for each bidder, indicating if their bid matches the highest bid
    # Each output is a flag (1 if the bid matches the highest bid, 0 otherwise), visible to the auctioneer
    placed_highest_bid = [
        Output((bids[i] == highest_bid).if_else(Integer(1), Integer(0)), f"bidder_{i}_placed_highest_bid", auctioneer)
        for i in range(5)
    ]

    # Return the highest bid and a list of flags indicating which bidders placed the highest bid
    return [Output(highest_bid, "highest_bid", auctioneer)] + placed_highest_bid