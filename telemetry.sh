#!/bin/bash

echo "[Optional] Enter your ETH address to enable nilup telemetry for your address."

# Read the user input
read user_eth_address
telemetry_base=nada-by-example-gitpod

# Check if the user input is empty
if [ -z "$user_eth_address" ]; then
    uuid=$(uuidgen)
    telemetry_id="$telemetry_base-$uuid"
    yes |  nilup instrumentation enable --wallet $telemetry_id
    echo "telemetry id: $telemetry_id"
else
    echo $user_eth_address
    telemetry_id="$telemetry_base-$user_eth_address"
    echo "telemetry id: $telemetry_id"
    nilup instrumentation enable --wallet $telemetry_id
fi

echo "Enjoy Nada by Example!"