#!/usr/bin/env bash

trap 'kill $(jobs -p)' EXIT
PORT=${1:-8091}
echo "Serving http server. $PORT"
python -m http.server --directory ./www $PORT &
WWW_PID=$$
cd src/ && python -m server
kill -s 9 ${WWW_PID}
echo "Safe Quit"
