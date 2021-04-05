#!/usr/bin/env bash

trap 'kill $(jobs -p)' EXIT
PORT=${1:-8091}
echo "Serving http server. $PORT"
python -m http.server --directory ./www $PORT &
cd src/ && python -m server
echo "Safe Quit"
