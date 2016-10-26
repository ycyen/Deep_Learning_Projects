#!/bin/bash
# ex. bash run_phase2.sh corpus/ptt_corpus.txt output_phase2/ 
echo Starting hw1 phase2:

#run code
python ptt2vec.py $1

#filter
python filterVocab.py fullVocab_phase2.txt < ptt2vec.txt > $2filter_vec.txt
