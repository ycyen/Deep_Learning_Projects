#!/bin/bash
# ex. bash run_phase1.sh corpus/text8 output_phase1/ 
echo Starting hw1 phase1:

#run code and filter
python word2vec_opt.py --train_data=$1
python filterVocab.py fullVocab.txt < word2vec.txt > $2filter_word2vec.txt

python glove.py $1
python filterVocab.py fullVocab.txt < glove.txt > $2filter_glove.txt
