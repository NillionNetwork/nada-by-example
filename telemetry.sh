#!/bin/bash

echo "Enabling nilup telemetry for nada-by-example"

telemetry_base=nada-by-example-gitpod

uuid=$(uuidgen)
telemetry_id="$telemetry_base-$uuid"
yes |  nilup instrumentation enable --wallet $telemetry_id
echo "nilup telemetry uuid: $telemetry_id"