#!/bin/bash

iterable="A E C B G F D B H A E B C G F B D H A B E C G B F D H B "
# input="A B D H X B F H B " # optional if we need to load 4 lines without changing cache
input="X B F H B "
for i in {1..1000}; do
    input+=${iterable}
done
input="${input%?}"

python3 plru_tree.py <<< "$input"
