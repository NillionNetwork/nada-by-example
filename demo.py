import yaml
import os
import sys
import streamlit as st
import ast

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
        # Extract the type (e.g., 'Integer') and value (e.g., '1')
        for value_type, actual_value in value.items():
            input_values[key] = int(actual_value)  # Convert to integer

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

def parse_program_code(program_code):
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
                if node.value.func.id in ['SecretInteger', 'PublicInteger', 'SecretBoolean']:  # Check for SecretInteger, PublicInteger, and SecretBoolean
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
    st.header(f"Program: {program_name}")
    st.write(f"Test: {nada_test_file_name}")

    # Get and parse the program code to find out who provides each input
    program_code = get_program_code(program_name)
    input_parties = parse_program_code(program_code)

    # Display the program code
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

    # Button to print the updated input values to the CLI with additional details
    if st.button('Print Updated Inputs to CLI'):
        for input_name, value in updated_input_values.items():
            party_name, input_type = input_parties.get(input_name, ('Unknown', 'Unknown'))
            print(f"Input: {input_name}, Value: {value}, Party: {party_name}, Type: {input_type}")
          
if __name__ == "__main__":
    main()