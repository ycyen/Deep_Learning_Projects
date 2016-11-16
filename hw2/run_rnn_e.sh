#!/bin/bash

inFile="./data/dataset_cnn_eng/testing_data.txt"
outFile="./predicition.upload"
#echo inputfile $1
#echo outputfile $2
bash setup.sh

python2 ./cs224d/assignment3/rnn_static_graph.py
