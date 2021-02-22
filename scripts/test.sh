#!/usr/bin/bash
echo "Testing"
cd src/ && python -m unittest -v tests/*
[[ "$?" != "0" ]] && exit 1
exit 0
