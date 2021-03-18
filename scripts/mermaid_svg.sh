#! /usr/bin/env bash

for file in docs/diagrams/*.seq ; do
    INPUT=$file
    OUTPUT=docs/wiki/assets/$(basename ${INPUT%.*}.svg)
    mkdir -p $(dirname $OUTPUT)
    npx mmdc -i $INPUT -o $OUTPUT
done
