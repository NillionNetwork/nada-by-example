# These tests use the nada-test testing framework
from nada_test import nada_test, NadaTest

# Functional style addition test
@nada_test(program="addition")
def addition_test_functional():
    num_1 = 30
    num_2 = 10
    inputs = {"num_1": num_1, "num_2": num_2}
    outputs = yield inputs
    assert outputs["sum"] == num_1 + num_2

# Class style addition test
@nada_test(program="addition")
class Test(NadaTest):
    def inputs(self):
        return {"num_1": 30, "num_2": 10}

    def check(self, outputs):
        assert outputs["sum"] == 40
