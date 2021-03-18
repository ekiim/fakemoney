#!/usr/bin/env bash
find . -name __pycache__ -type d | xargs rm -rf
rm -rf ./www/docs
rm ./docs/diagrams/*.svg
rm ./src/server.log
rm ./src/.coverage
rm .docker_id
