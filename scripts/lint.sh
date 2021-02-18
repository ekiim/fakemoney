#!/usr/bin/bash
echo "Linting"
flake8 \
    --ignore E731 \
    src/
echo "Finish linting"
