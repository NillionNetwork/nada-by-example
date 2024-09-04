from nada_test import nada_test

inputs = {"num_0": 10, "num_1": 20, "num_2": 30, "num_3": 40}

# Test that the shuffled array contains the same values as the input, regardless of order
@nada_test(program="shuffle_simple")
def shuffle_simple_test_same_values():
    outputs = yield inputs

    shuffled_nums = [
        outputs["shuffled_num_0"], 
        outputs["shuffled_num_1"], 
        outputs["shuffled_num_2"], 
        outputs["shuffled_num_3"]
    ]
    
    # Assert that the sorted output contains the same values as the sorted input
    assert sorted(shuffled_nums) == sorted([
        inputs["num_0"], 
        inputs["num_1"], 
        inputs["num_2"], 
        inputs["num_3"]
    ]), "Test failed: the shuffled array contains different values."

# Test that the resulting shuffled array is not in the same order as the input
@nada_test(program="shuffle_simple")
def shuffle_simple_test_not_same_order():
    outputs = yield inputs

    original_nums = [
        inputs["num_0"], 
        inputs["num_1"], 
        inputs["num_2"], 
        inputs["num_3"]
    ]

    shuffled_nums = [
        outputs["shuffled_num_0"], 
        outputs["shuffled_num_1"], 
        outputs["shuffled_num_2"], 
        outputs["shuffled_num_3"]
    ]

    # Assert that the shuffled numbers are NOT in the same order as the input
    assert shuffled_nums != original_nums, "Test failed: the order did not change"
