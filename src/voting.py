from nada_dsl import *
import nada_numpy as na

# Candidate mapping: candidate name to their respective candidate identifier
# Every voter reads the candidate map and casts their vote. 
# If their vote is SecretInteger: 1, it means they cast a vote for kamala_harris
# If their vote is SecretInteger: 2, it means they cast a vote for donald_trump
# If their vote is SecretInteger: 3, it means they cast a vote for rfk_jr
candidates_map = {"kamala_harris": 1, "donald_trump": 2, "rfk_jr": 3}

def count_votes_for_candidate(votes: List[SecretInteger], initialValue: SecretInteger, candidate_id: Integer) -> SecretInteger:
    total_votes_for_candidate = initialValue
    for vote in votes:
        votes_to_add = (vote == candidate_id).if_else(Integer(1), Integer(0))
        # print(type(votes_to_add)) # every voter's vote is kept secret: <class 'nada_dsl.nada_types.types.SecretInteger'>
        total_votes_for_candidate = total_votes_for_candidate + votes_to_add
    
    return total_votes_for_candidate

def nada_main():
    num_voters = 8
    # Creates parties with names Voter0, Voter1 ... Voter7
    voters = na.parties(num_voters, [f"Voter{i}" for i in range(num_voters)])
    party_official = Party(name="Official")
    vote_start_count = SecretInteger(Input(name="vote_start_count", party=party_official))

    votes_list = []
    for i in range(num_voters):
        votes_list.append(
            # Voter0 inputs vote_0
            SecretInteger(Input(name="vote_" + str(i), party=voters[i]))
        )

    # Get the total votes per candidate
    candidate_totals = {
        name: count_votes_for_candidate(votes_list, vote_start_count, Integer(candidate_id))
        for name, candidate_id in candidates_map.items()
    }

    vote_count_results = [
        Output(candidate_totals[name], f"{name}_votes", party=party_official)
        for name in candidates_map.keys()
    ]
    return vote_count_results

if __name__ == "__main__":
   nada_main()