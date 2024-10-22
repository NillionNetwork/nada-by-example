import yaml
import json
import os
import sys
import streamlit as st
import asyncio
from nillion_client_script import store_inputs_and_run_blind_computation

def parse_nada_yaml_test_file(file_path):
    """
    Parse a YAML test file for a Nada program.
    
    Args:
    file_path (str): Path to the YAML file.
    
    Returns:
    tuple: Contains program_name (str), input_values (dict), and expected_outputs (dict).
    """
    with open(file_path, 'r') as file:
        yaml_content = file.read()

    yaml_data = yaml.safe_load(yaml_content)

    program_name = yaml_data.get('program', '')
    input_values = yaml_data.get('inputs', {})
    expected_outputs = yaml_data.get('expected_outputs', {})

    return program_name, input_values, expected_outputs

def get_program_code(program_name):
    """
    Retrieve the source code of a Nada program.
    
    Args:
    program_name (str): Name of the program.
    
    Returns:
    str: The program's source code or an error message if the file is not found.
    """
    program_file_path = os.path.join("src", f"{program_name}.py")

    if os.path.exists(program_file_path):
        with open(program_file_path, 'r') as file:
            program_code = file.read()
        return program_code
    else:
        return f"Error: Program file '{program_name}.py' not found in 'src' directory."
    
def get_program_json(program_name, local_path=None):
    """
    Retrieve the JSON representation of a compiled Nada program.
    
    Args:
    program_name (str): Name of the program.
    local_path (str, optional): Custom path to look for the program JSON file. 
                                If None, defaults to the 'target' directory.
    
    Returns:
    str: The program's JSON representation or an error message if the file is not found.
    """
    if local_path:
        program_file_path = local_path
    else:
        program_file_path = os.path.join("target", f"{program_name}.nada.json")

    if os.path.exists(program_file_path):
        with open(program_file_path, 'r') as file:
            program_code = file.read()
        return program_code
    else:
        if local_path:
            return f"Error: Program json '{program_name}.nada.json' not found in '{local_path}' directory."
        else:
            return f"Error: Program json '{program_name}.nada.json' not found in 'target' directory."
        
def parse_nada_json(json_data):
    """
    Parse the JSON representation of a Nada program to extract input and output information.
    
    Args:
    json_data (str or dict): JSON data of the program.
    
    Returns:
    tuple: Contains input_info (dict) and output_info (dict).
    """
    if isinstance(json_data, str):
        json_data = json.loads(json_data)
    
    input_info = {}
    for input_data in json_data.get('inputs', []):
        input_name = input_data['name']
        input_info[input_name] = {
            'type': input_data['type'],
            'party': input_data['party']
        }
    
    output_info = {}
    for output_data in json_data.get('outputs', []):
        output_name = output_data['name']
        output_info[output_name] = {
            'type': output_data['type'],
            'party': output_data['party']
        }
    
    return input_info, output_info

import streamlit as st

def create_party_inputs(input_info, input_values):
    party_names = sorted(set(info['party'] for info in input_info.values()))
    updated_input_values = input_values.copy()

    if len(party_names) > 1:
        # Create two columns if there's more than one party
        columns = st.columns(2)
    else:
        # Create a single column if there's only one party
        columns = [st.columns(1)[0]]

    # Distribute parties between the columns
    for i, party_name in enumerate(party_names):
        with columns[i % len(columns)]:
            st.subheader(f"{party_name}'s inputs")
            for input_name, value in input_values.items():
                if input_info[input_name]['party'] == party_name:
                    input_type = input_info[input_name]['type']
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

    return updated_input_values

def main(nada_test_file_name=None, path_nada_bin=None, path_nada_json=None):
    # pass test name in via the command line
    if nada_test_file_name is None:
        if len(sys.argv) != 2:
            st.write("Usage: streamlit run streamlit_app.py <nada_test_file_name>")
            sys.exit(1)
        nada_test_file_name = sys.argv[1]

    # Construct the YAML file path based on the provided file name
    yaml_file_path = os.path.join("tests", f"{nada_test_file_name}.yaml")

    # Check if the YAML file exists
    if not os.path.exists(yaml_file_path):
        st.error(f"YAML file not found: {yaml_file_path}")
        sys.exit(1)

    # Parse the YAML file
    program_name, input_values, expected_outputs = parse_nada_yaml_test_file(yaml_file_path)

    # Get the program code
    program_code = get_program_code(program_name)
    program_json_data = get_program_json(program_name, path_nada_json)
    input_info, output_info = parse_nada_json(program_json_data)

    # Display the program name and test name
    st.header(f"Nada Program Demo: {program_name}")

    st.caption(f"This is a demo of the `{program_name}.py` Nada program running on the [Nillion Testnet](https://docs.nillion.com/network-configuration#testnet). Initial input values to the program come from the `{nada_test_file_name}.yaml` test file. Check out more examples within Nada by Example [Docs](https://docs.nillion.com/nada-by-example) and [Github Repo](https://github.com/NillionNetwork/nada-by-example)")

    cluster_id_from_streamlit_config = st.secrets.get("cluster_id", None)
    grpc_endpoint_from_streamlit_config = st.secrets.get("grpc_endpoint", None)
    chain_id_from_streamlit_config = st.secrets.get("chain_id", None)
    bootnodes_str_from_streamlit_config = st.secrets.get("bootnode", None)
    bootnodes = [bootnodes_str_from_streamlit_config] if bootnodes_str_from_streamlit_config else None

    # Add a toggle section for configuration values
    if all([cluster_id_from_streamlit_config, grpc_endpoint_from_streamlit_config, chain_id_from_streamlit_config, bootnodes]):
        with st.expander("Nillion Network Configuration"):
            st.text("PetNet Cluster ID")
            st.code(cluster_id_from_streamlit_config)
            st.text("PetNet Bootnodes")
            st.code(bootnodes_str_from_streamlit_config)
            st.text("NilChain GRPC Endpoint")
            st.code(grpc_endpoint_from_streamlit_config)
            st.text("NilChain Chain ID")
            st.code(chain_id_from_streamlit_config)

    # Display the program code
    st.subheader(f"{program_name}.py")
    with st.expander(f"Nada Program: {program_name}"):
        st.code(program_code, language='python')

    # Display inputs grouped by party, alphabetized
    updated_input_values = create_party_inputs(input_info, input_values)
    
    output_parties = list(set(output['party'] for output in output_info.values()))

    should_store_inputs = st.checkbox("Store secret inputs before running blind computation", value=False)

    # Button to store inputs with a loading screen
    if st.button('Run blind computation'):
        st.divider()
        # Conditional spinner text
        if should_store_inputs:
            spinner_text = "Storing the Nada program, storing inputs, and running blind computation on the Nillion Network Testnet..."
        else:
            spinner_text = "Storing the Nada program and running blind computation with computation-time secrets on the Nillion Network Testnet..."
        
        # Run the async function with spinner
        with st.spinner(spinner_text):
            # Prepare the input data to pass to the second file
            input_data = {}
            for input_name, value in updated_input_values.items():
                party_name = input_info[input_name]['party']
                input_type = input_info[input_name]['type']
                input_data[input_name] = (value, party_name, input_type)
            
            # Add your Nilchain private key to the .streamlit/secrets.toml file
            nilchain_private_key=st.secrets["nilchain_private_key"]

            # Call the async store_inputs_and_run_blind_computation function and wait for it to complete
            result_message = asyncio.run(store_inputs_and_run_blind_computation(input_data, program_name, output_parties, nilchain_private_key, path_nada_bin, cluster_id_from_streamlit_config, grpc_endpoint_from_streamlit_config, chain_id_from_streamlit_config, bootnodes, should_store_inputs))

        st.subheader("Nada Program Result")

        # st.text('Output(s)')
        st.success('Output(s)', icon="🖥️")
        st.caption(f"The Nada program returned one or more outputs to designated output parties - {output_parties}")
        st.json(result_message['output'])

        st.text('Nilchain Nillion Address')
        st.caption(f"Blind computation ran on the Nillion PetNet and operations were paid for on the Nilchain Testnet. Check out the Nilchain transactions that paid for each PetNet operation (store program, store secrets, compute) on the [Nillion Testnet Explorer](https://testnet.nillion.explorers.guru/account/{result_message['nillion_address']})")
        st.code(result_message['nillion_address'], language='json')
        
        st.text('Store IDs')
        st.caption('The Store IDs are the unique identifiers used to reference input values you stored in the Nillion Network on the PetNet.')
        st.code(result_message['store_ids'], language='json')

        st.text('User Key')
        st.caption(f"The user key is a private key derived from a PetNet user public/private key pair. It is randomized every time you run this page for the sake of the demo, ensuring that the key is different for each session.")
        st.code(result_message['user_key'], language='json')

        st.text('User ID')
        st.caption(f"The user id is derived from your PetNet user key and serves as your public user identifier on the Nillion Network. Since the user key is randomized with each run of the demo, the user id is also randomized accordingly.")
        st.code(result_message['user_id'], language='json')

        st.text('Program ID')
        st.caption('The Program ID is the identifier for the program you stored in the Nillion Network on the PetNet. The Program ID naming convention is your [user_id]/[program_name]')
        st.code(result_message['program_id'], language='json')
        
        st.balloons()
      
if __name__ == "__main__":
    main()