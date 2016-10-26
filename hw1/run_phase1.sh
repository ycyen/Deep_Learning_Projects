#!/bin/bash
# ex. bash run_phase1.sh corpus/text8 output_phase1/ 
echo Hw1 phase1:
mkdir $2
mkdir tmp

#run code and filter
echo Start Word2Vec
python word2vec_opt.py --train_data=$1
python filterVocab.py fullVocab.txt < tmp/word2vec.txt > $2filter_word2vec.txt

echo Start Glove
python glove.py $1
python filterVocab.py fullVocab.txt < tmp/glove.txt > $2filter_glove.txt

rm -r tmp
