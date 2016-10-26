#!/bin/bash
# ex. bash run_phase2.sh corpus/ptt_corpus.txt output_phase2/ 
echo Hw1 phase2:
mkdir $2
mkdir tmp

#run code
python ptt2vec.py --train_data=$1

#filter
python filterVocab.py fullVocab_phase2.txt < tmp/ptt2vec.txt > $2filter_vec.txt

rm -r tmp