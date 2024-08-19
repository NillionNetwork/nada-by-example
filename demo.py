import yaml
import os
import sys
import streamlit as st
import ast
import asyncio
from nillion_client_script import store_inputs_and_run_blind_computation

def parse_nada_test_file(file_path):
    # Open and read the YAML file
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Get the Nada program name
    program_name = data.get('program', '')

    # Get Nada inputs and their test values
    inputs = data.get('inputs', {})
    input_values = {}

    for key, value in inputs.items():
        for value_type, actual_value in value.items():
            input_values[key] = int(actual_value)

    return program_name, input_values

def get_program_code(program_name):
    # Construct the path to the program file
    program_file_path = os.path.join("src", f"{program_name}.py")

    # Check if the program file exists
    if os.path.exists(program_file_path):
        # Open and read the program file
        with open(program_file_path, 'r') as file:
            program_code = file.read()
        return program_code
    else:
        return f"Error: Program file '{program_name}.py' not found in 'src' directory."

def parse_program_code_for_inputs(program_code):
    # Parse the Python code to find out who gives each input
    tree = ast.parse(program_code)
    input_parties = {}
    party_map = {}

    class PartyVisitor(ast.NodeVisitor):
        def visit_Assign(self, node):
            # Map party variables to their names, e.g., party_alice = Party(name="Alice")
            if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'Party':
                party_var = node.targets[0].id
                for keyword in node.value.keywords:
                    if keyword.arg == "name" and isinstance(keyword.value, ast.Constant):
                        party_map[party_var] = keyword.value.value
            self.generic_visit(node)

    class InputPartyVisitor(ast.NodeVisitor):
        def visit_Assign(self, node):
            # Link input names to parties, e.g., should_double = SecretBoolean(Input(name="should_double", party=party_alice))
            if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
                if node.value.func.id in ['SecretInteger', 'PublicInteger', 'SecretBoolean', 'PublicBoolean', 'SecretUnsignedInteger', 'PublicUnsignedInteger']:  # Check for SecretInteger, PublicInteger, and SecretBoolean
                    input_name = node.targets[0].id
                    for keyword in node.value.args[0].keywords:
                        if keyword.arg == "party" and isinstance(keyword.value, ast.Name):
                            party_var = keyword.value.id
                            party_name = party_map.get(party_var, "Unknown")
                            input_parties[input_name] = (party_name, node.value.func.id)  # Store both party name and input type
            self.generic_visit(node)

    # Visit the tree to populate the party_map and input_parties
    PartyVisitor().visit(tree)
    InputPartyVisitor().visit(tree)

    return input_parties

def parse_program_code_for_output_parties(program_code):
    tree = ast.parse(program_code)
    output_parties = []

    class OutputPartyVisitor(ast.NodeVisitor):
        def visit_Call(self, node):
            # Check if the call is to the 'Output' class
            if isinstance(node.func, ast.Name) and node.func.id == 'Output':
                # The last argument of Output is typically the party
                party_arg = node.args[-1]
                if isinstance(party_arg, ast.Name):
                    # Look for the assignment where the Party instance was created
                    for n in ast.walk(tree):
                        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id == party_arg.id:
                            party_instance = n.value
                            if isinstance(party_instance, ast.Call) and isinstance(party_instance.func, ast.Name) and party_instance.func.id == 'Party':
                                # Extract the party name
                                for keyword in party_instance.keywords:
                                    if keyword.arg == "name" and isinstance(keyword.value, ast.Constant):
                                        party_name = keyword.value.value
                                        output_parties.append(party_name)
            self.generic_visit(node)

    OutputPartyVisitor().visit(tree)
    return output_parties

def main():
    # Look for the test name to use in the demo
    if len(sys.argv) != 2:
        st.write("Usage: python3 demo.py <nada_test_file_name>")
        sys.exit(1)

    # Get the YAML file name from the command line argument
    nada_test_file_name = sys.argv[1]

    # Construct the YAML file path based on the provided file name
    yaml_file_path = os.path.join("tests", f"{nada_test_file_name}.yaml")

    # Parse the YAML file
    program_name, input_values = parse_nada_test_file(yaml_file_path)

    # Display the program name and test name
    st.header(f"Nada Program Demo: {program_name}")

    st.caption(f"This is a demo of the `{program_name}.py` Nada program running on the [Nillion Testnet](https://docs.nillion.com/network-configuration#testnet). Initial input values to the program come from the `{nada_test_file_name}.yaml` test file. Check out more examples within Nada by Example [Docs](https://docs.nillion.com/nada-by-example) and [Github Repo](https://github.com/NillionNetwork/nada-by-example)")

    # Get and parse the program code to find out who provides each input
    program_code = get_program_code(program_name)
    input_parties = parse_program_code_for_inputs(program_code)

    # Display the program code
    st.subheader(f"{program_name}.py")
    st.code(program_code, language='python')

    # Group inputs by party
    party_inputs = {}
    for input_name, value in input_values.items():
        party_name, input_type = input_parties.get(input_name, ('Unknown', 'Unknown'))
        if party_name not in party_inputs:
            party_inputs[party_name] = []
        party_inputs[party_name].append((input_name, value, input_type))

    # Display inputs grouped by party
    updated_input_values = {}
    for party_name, inputs in party_inputs.items():
        st.subheader(f"{party_name}'s Inputs")
        for input_name, value, input_type in inputs:
            if input_type == 'SecretBoolean':
                updated_input_values[input_name] = st.checkbox(
                    label=f"{input_type}: {input_name}",
                    value=bool(value)
                )
            else:
                updated_input_values[input_name] = st.number_input(
                    label=f"{input_type}: {input_name}",
                    value=value
                )
    
    output_parties = parse_program_code_for_output_parties(program_code)

    # Button to store inputs with a loading screen
    if st.button('Run blind computation'):
        with st.spinner(f"Storing the Nada program, storing inputs, and running blind computation on the Nillion Network Testnet..."):
            # Prepare the input data to pass to the second file
            input_data = {}
            for input_name, value in updated_input_values.items():
                party_name, input_type = input_parties.get(input_name, ('Unknown', 'Unknown'))
                input_data[input_name] = (value, party_name, input_type)
            
            # Add your Nilchain private key to the .streamlit/secrets.toml file
            nilchain_private_key=st.secrets["nilchain_private_key"]

            # Call the async store_inputs_and_run_blind_computation function and wait for it to complete
            result_message = asyncio.run(store_inputs_and_run_blind_computation(input_data, program_name, output_parties, nilchain_private_key))

        st.divider()

        st.subheader("Nada Program Result")
        st.success(f"Blind computation on the {program_name} program is complete!", icon="🙈")
        st.text('Output(s)')
        st.caption(f"A Nada program returns one or more outputs to designated output parties - {output_parties}")
        st.code(result_message['output'], language='json')
        
        st.text('Store IDs')
        st.caption('The Store IDs are the unique identifiers used to reference input values you stored in the Nillion Network on the PetNet.')
        st.code(result_message['store_ids'], language='json')

        st.text('PetNet User ID')
        st.caption(f"The User ID is derived from your PetNet user public/private key pair and serves as your public user identifier on the Nillion Network. The user key is randomized every time you run this demo, so the User ID is also randomized.")
        st.code(result_message['user_id'], language='json')

        st.text('Program ID')
        st.caption('The Program ID is the identifier for the program you stored in the Nillion Network on the PetNet. The Program ID naming convention is your [user_id]/[program_name]')
        st.code(result_message['program_id'], language='json')
        
        st.text('Nilchain Nillion Address')
        st.caption(f"Blind computation ran on the Nillion PetNet and operations were paid for on the Nilchain Testnet. Check out the Nilchain transactions that paid for each PetNet operation (store program, store secrets, compute) on the [Nillion Testnet Explorer](https://testnet.nillion.explorers.guru/account/{result_message['nillion_address']})")
        st.code(result_message['nillion_address'], language='json')
        st.balloons()
      
if __name__ == "__main__":
    main()