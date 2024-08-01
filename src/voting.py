from nada_dsl import *
import nada_numpy as na

def count_votes_for_candidate(array: List[SecretInteger], initialValue: SecretInteger, candidate_num: Integer) -> SecretInteger:
    total_votes_for_candidate = initialValue
    for element in array:
        votes_to_add = (element == candidate_num).if_else(Integer(1), Integer(0))
        # print(type(votes_to_add)) # votes are kept secret: <class 'nada_dsl.nada_types.types.SecretInteger'>
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

    # Candidate mapping: candidate name to their respective identifier
    # if a voter casts a vote that is SecretInteger: 3, it means they are voting for rfk jr
    candidates_map = {"kamala_harris": 1, "donald_trump": 2, "rfk_jr": 3}

    # Get the total votes per candidate
    candidate_totals = {
        name: count_votes_for_candidate(votes_list, vote_start_count, Integer(identifier))
        for name, identifier in candidates_map.items()
    }

    vote_count_results = [
        Output(candidate_totals[name], f"{name}_votes", party=party_official)
        for name in candidates_map.keys()
    ]
    return vote_count_results

if __name__ == "__main__":
   nada_main()