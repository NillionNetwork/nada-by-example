from nada_test import nada_test, NadaTest

# test FAILING
@nada_test(program="main")
def test_addition():
    a, b = 1, 2
    return {
        "inputs": {"A": a, "B": b},
        "expected_outputs": {"my_output": a + b}
    }

# test with yield: PASSING
@nada_test(program="main")
def test_addition_with_yield():
    a, b = 1, 2
    inputs = {"A": a, "B": b}
    expected_outputs = {"my_output": a + b}
    outputs = yield inputs
    assert outputs == expected_outputs

# class based test: PASSING
@nada_test(program="main")
class test_addition_class_based(NadaTest):
    def inputs(self):
        return {"A": 1, "B": 2}

    def check(self, outputs):
        assert outputs["my_output"] == 3