#!/bin/bash

#python translate.py --data_dir data_1 --train_dir test1210\
#	--en_vocab_size=40000 --fr_vocab_size=40000
echo translating $1 ...
python translate.py --decode --data_dir data_1 --train_dir test1204\
	--en_vocab_size=40000 --fr_vocab_size=40000 < $1 > answer.tmp
echo done!
tail -n +2 answer.tmp | cut -c 3- > $2
rm answer.tmp
