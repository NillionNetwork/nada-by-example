# Nada by Example

This is an introduction to Nillion's [Nada language](https://docs.nillion.com/nada-lang) with examples of all [built-in operations](https://docs.nillion.com/nada-lang-operators).

## Run Examples

### 1-Click Setup with Gitpod

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/nillionnetwork/nada-by-example)

Open nada-by-example in Gitpod, then run any example

```
nada run [test-name]
```

#### After 1-click setup, run an example in the streamlit demo app

1. Add your Nilchain private key in the .streamlit/secrets.toml file

2. Run a demo

```
streamlit run streamlit.py [test-name]
```

### Local Installation Instructions

#### 1. Install Nillion

Install nilup

```
curl https://nilup.nilogy.xyz/install.sh | bash
```

Install the `latest` version of the Nillion SDK and tools

```
nilup install latest
nilup use latest
```

#### 2. Create Python virtual environment and install Nada

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### 3. Optionally enable nilup telemetry, providing your Ethereum wallet address.

```
nilup instrumentation enable --wallet <your-eth-wallet-address>
```

### Build (compile) all Nada programs

```
nada build
```

This creates one compiled binary (.nada.bin) file per program listed in the `nada-project.toml` file in the target/ directory.

### Test a Nada program

```
nada test [test_name]
```

For example to test the `src/addition.py` program with the test value inputs from `tests/addition_test.yaml`, run:

```
nada test addition_test
```

## Add a New Example

### 1. Create a new Nada program

Create a new file in `src/` with the name of the program.

Write the program in the new file

### 2. Add your program to nada-project.toml config file

For the nada tool to know about the new program, you need to add the following to the to the `nada-project.toml` config file. Change this code so the `path` and `name` match the name of your program.

```
[[programs]]
path = "src/your_program_name.py"
name = "your_program_name"
prime_size = 128
```

### 3. Generate test

Use the nada tool to generate a set of test values for your program, that will be stored in `tests/`.

```
nada generate-test --test-name {your_program_name}_test {your_program_name}
```

### 4. Test your program

```
nada test {your_program_name}_test
```

Test the program. If you run the above command without altering the default values (3s) in the test file (tests/{your_program_name}\_test.yaml), the test will fail because the expected test output doesn't match the resulting output. Modify the values in the test file and re-test the program.

### Run a Streamlit App on Nillion Testnet

### 1. Install dependencies

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Create a streamlit secrets file and add your nilchain private key within `.streamlit/secrets.toml`

```
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

### 3. Run the `addition` test with starter values from `addition_test`

```
streamlit run streamlit_app.py addition_test
```

### 4. Run any other example that isn't using na.numpy or loops to define input and output parties

```
streamlit run streamlit.py [test-name]
```
