import asyncio
import py_nillion_client as nillion
import uuid

from py_nillion_client import NodeKey, UserKey
from nillion_python_helpers import get_quote_and_pay, create_nillion_client, create_payments_config

from cosmpy.aerial.client import LedgerClient
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey

# Nillion Testnet Config: https://docs.nillion.com/network-configuration#testnet
cluster_id = 'b13880d3-dde8-4a75-a171-8a1a9d985e6c'
grpc_endpoint = '65.109.228.73:9090'
chain_id = 'nillion-chain-testnet-1'
bootnode = '/dns/node-1.testnet-photon.nillion-network.nilogy.xyz/tcp/14111/p2p/12D3KooWCfFYAb77NCjEk711e9BVe2E6mrasPZTtAjJAPtVAdbye'
bootnodes = [bootnode]

async def store_inputs_and_run_blind_computation(input_data, program_name, output_parties, nilchain_private_key):
    # Create Nillion Client for user
    seed=str(uuid.uuid4())
    userkey = UserKey.from_seed(f"nada-by-example-{seed}")

    nodekey = NodeKey.from_seed(seed)
    client = create_nillion_client(userkey, nodekey, bootnodes)

    party_id = client.party_id
    user_id = client.user_id

    # Pay for and store the program
    # Set the program name and path to the compiled program
    program_mir_path = f"./target/{program_name}.nada.bin"
    # Create payments config, client and wallet
    payments_config = create_payments_config(chain_id, grpc_endpoint)
    payments_client = LedgerClient(payments_config)

    # Check that private key is set in the streamlit secrets file
    try:
        private_key = PrivateKey(bytes.fromhex(nilchain_private_key))
        print("Using Nilchain private key...")
    except Exception as e:
        raise RuntimeError(f"Invalid Nilchain private key! Before running blind computation, set your Nilchain Testnet nilchain_private_key within the .streamlit/secrets.toml secrets file.")
    
    payments_wallet = LocalWallet(
        private_key,
        prefix="nillion",
    )

    # Pay to store the program and obtain a receipt of the payment
    memo_store_program = f"petnet operation: store_program; program_name: {program_name}; user_id: {user_id}"
    receipt_store_program = await get_quote_and_pay(
        client,
        nillion.Operation.store_program(program_mir_path),
        payments_wallet,
        payments_client,
        cluster_id,
        memo_store_program,
    )
    print(f"🧾 RECEIPT MEMO: {memo_store_program}")

    # Store the program
    program_id = await client.store_program(
        cluster_id, program_name, program_mir_path, receipt_store_program
    )

    print(program_id)

    compute_bindings = nillion.ProgramBindings(program_id)

    for party_name in output_parties:
        compute_bindings.add_output_party(party_name, party_id)

    store_ids=[]
    # Store each input
    for input_name, details in input_data.items():
        value, party_name, input_type = details
        print(f"Processing Input: {input_name}, Value: {value}, Party: {party_name}, Type: {input_type}")
        
        # Nada types to Nillion types
        types_mapping = {
            # Integers
            'SecretInteger': nillion.SecretInteger,
            'PublicInteger': nillion.Integer,
            # Unsigned Integers
            'SecretUnsignedInteger': nillion.SecretUnsignedInteger,
            'PublicUnsignedInteger': nillion.UnsignedInteger,
            # Booleans
            'SecretBoolean': nillion.SecretBoolean,
            'PublicBoolean': nillion.Boolean,
        }

        nada_val = types_mapping.get(input_type, nillion.Integer)(value)

        new_secret = nillion.NadaValues(
            {
                input_name: nada_val
            }
        )

        memo_store_values = f"petnet operation: store_values; name: {input_name}; user_id: {user_id}"
        receipt_store = await get_quote_and_pay(
            client,
            nillion.Operation.store_values(new_secret, ttl_days=5),
            payments_wallet,
            payments_client,
            cluster_id,
            memo_store_values,
        )
        print(f"🧾 RECEIPT MEMO: {memo_store_values}")

        # Set permissions for the client to compute on the program
        permissions = nillion.Permissions.default_for_user(client.user_id)
        permissions.add_compute_permissions({client.user_id: {program_id}})
        compute_bindings.add_input_party(party_name, party_id)

        store_id = await client.store_values(
            cluster_id, new_secret, permissions, receipt_store
        )
        print(input_name, store_id)
        store_ids.append(store_id)
        print(store_ids)

        await asyncio.sleep(1)  # Simulate async delay for each input
    
    computation_time_secrets = nillion.NadaValues({})

    memo_compute = f"petnet operation: compute; program_id: {program_id}; user_id: {user_id}"
    # Pay for the compute
    receipt_compute = await get_quote_and_pay(
        client,
        nillion.Operation.compute(program_id, computation_time_secrets),
        payments_wallet,
        payments_client,
        cluster_id,
        memo_compute,
    )
    print(f"🧾 RECEIPT MEMO: {memo_compute}")

    # Compute on the secrets
    compute_id = await client.compute(
        cluster_id,
        compute_bindings,
        store_ids,
        computation_time_secrets,
        receipt_compute,
    )

    print(f"The computation was sent to the network. compute_id: {compute_id}")
    while True:
        compute_event = await client.next_compute_event()
        if isinstance(compute_event, nillion.ComputeFinishedEvent):
            print(f"✅  Compute complete for compute_id {compute_event.uuid}")
            print(compute_event)
            print(compute_event.result)
            blind_computation_results = compute_event.result.value
            return {
                'user_id': user_id,
                'program_id': program_id,
                'store_ids': store_ids, 
                'output': blind_computation_results,
                'nillion_address': payments_wallet,      
            }
        