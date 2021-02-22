#!/usr/bin/env bash
find . -name __pycache__ -type d | xargs rm -rf
rm ./docs/diagrams/*.svg
rm ./src/server.log
rm .docker_id
