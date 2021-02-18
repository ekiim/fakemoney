#!/usr/bin/env bash
find . -name __pycache__ -type d | xargs rm -rf
rm ./src/server.log
rm .docker_id
