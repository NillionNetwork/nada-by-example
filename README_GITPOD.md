# Welcome to Nada by Example

This Gitpod environment is set up with everything you need to run and test the example programs in [Nada by Example](https://docs.nillion.com/nada-by-example).

## How to run an example program

Every Nada program example has a corresponding test file. Programs are in [`nada-by-example/src/`](https://github.com/NillionNetwork/nada-by-example/tree/main/src) and test files are in [`nada-by-example/tests`](https://github.com/NillionNetwork/nada-by-example/tree/main/tests). Running a program uses the inputs specified in the test file. Testing a program uses the inputs specified in the test file and also checks the outputs against the `expected_outputs` specified in the test file.

Run any program with the inputs specified in the test file with [`nada run`](/nada#run-a-program)

```
nada run <test-file-name>
```

To run the addition program with `addition_test` test inputs:

```
nada run addition_test
```

The result of running this program is

```
(.venv) ➜  nada-by-example git:(main) nada run addition_test
Running program 'addition' with inputs from test file addition_test
Building ...
Running ...
Program ran!
Outputs: {
    "sum": SecretInteger(
        NadaInt(
            40,
        ),
    ),
}
```

## How to test an example program

Test any program with the inputs and outputs specified in the test file with [`nada test`](/nada#test-a-program)

```
nada test <test-file-name>
```

Test the addition program with `addition_test` test inputs and expected outputs:

```
nada test addition_test
```

The result of testing this program is

```
(.venv) ➜  nada-by-example git:(main) nada test addition_test
Running test: addition_test
Building ...
Running ...
addition_test: PASS
```

Testing the addition program with `addition_test` results in a PASS because the expected_outputs `sum` output matches the run result.

## How to add a new test for the addition example

Use the [nada tool](/nada#generate-a-test-file) to add a new test file named "addition_test_2" for the addition example.

```
nada generate-test --test-name addition_test_2 addition
```

This results in a new test file: `/tests/addition_test_2.yaml`

```
(.venv) ➜  nada-by-example git:(main) nada generate-test --test-name addition_test_2 addition
Generating test 'addition_test_2' for
Building ...
Generating test file ...
Test generated!
```

Update the values in the test file to anything you want, for example:

```yaml
---
program: addition
inputs:
  num_1:
    SecretInteger: '100'
  num_2:
    SecretInteger: '10'
expected_outputs:
  sum:
    SecretInteger: '110'
```

### Run addition with your new test

```
nada run addition_test_2
```

### Test addition with your new test

```
nada test addition_test_2
```

## Keep exploring examples

🥳 You're all set up to run and test any example in [nada-by-example](https://github.com/NillionNetwork/nada-by-example). Keep exploring what's possible with Nada by running the rest of the programs in the repo.
