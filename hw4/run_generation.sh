#!/bin/bash
#time python translate.py --data_dir NLG_data --train_dir nlg_model\
#	--en_vocab_size=40000 --fr_vocab_size=40000
echo parsing test data ...
python ./NLG_data/parse_test.py $1

echo translating $1 ...
python translate.py --decode --data_dir NLG_data --train_dir nlg_model\
	--en_vocab_size=40000 --fr_vocab_size=40000 < test.tmp > answer.tmp
echo done!
tail -n +2 answer.tmp | cut -c 3- > $2
rm answer.tmp
#rm test.tmp
