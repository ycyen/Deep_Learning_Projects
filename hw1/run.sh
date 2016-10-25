#!/bin/bash
echo Starting hw1

#phase1
echo phase1:

cd corpus
unzip text8.zip
cd ..

#run code
#python word2vec_opt.py
#python glove.py

#filter
python filterVocab.py fullVocab.txt < word2vec.txt > ./output/filter_word2vec.txt
python filterVocab.py fullVocab.txt < glove.txt > ./output/filter_glove.txt
cd output

#zip file
zip submission filter_word2vec.txt filter_glove.txt
cd ..

#phase2
echo phase2:

cd corpus
unzip ptt_corpus.zip
cd ..

#run code
#python ptt2vec.py

#filter
python filterVocab.py fullVocab_phase2.txt < ptt2vec.txt > ./output/filter_vec.txt
cd output

#zip file
zip submission filter_vec.txt
cd ..