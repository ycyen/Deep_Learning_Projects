#!/bin/bash

inFile="./data/dataset_cnn_eng/testing_data.txt"
outFile="./predicition.upload"
#echo inputfile $1
#echo outputfile $2

python3 ./cnn-text-classification-tf/my_eval.py --checkpoint_dir="./cnn-text-classification-tf/runs/1478963932/checkpoints/" --data_file="$inFile" --out_file="$outFile"
