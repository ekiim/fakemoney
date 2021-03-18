#!/usr/bin/env bash

PORT=${1:-8091}
echo "Serving http server. $PORT"
python -m http.server --directory ./www $PORT
