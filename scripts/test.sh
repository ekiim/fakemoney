#!/usr/bin/bash
echo "Testing"
ERROR=0
cd src && coverage run --source="./" --omit="./tests" -m unittest -v tests/*
[[ "$?" != "0" ]] && ERROR=1
coverage report
coverage html -d  ../www/docs/python
exit $ERROR
