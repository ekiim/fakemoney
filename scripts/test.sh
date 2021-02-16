#!/usr/bin/bash
echo "testing"
cd src/ && python -m unittest -v tests/*
[[ "$?" != "0" ]] && exit 1
exit 0
