#!/bin/bash
#bash run_intent.sh \[testing data\] \[answer file\]
python3 parse.test.py $1

data_dir=data/ATIS_hw3
model_dir=model_hw3
max_sequence_length=50  # max length for train/valid/test sequence
task=joint  # available options: intent; tagging; joint
bidirectional_rnn=True  # available options: True; False

python3 run_multi-task_rnn.py --data_dir $data_dir \
      --train_dir   $model_dir\
      --max_sequence_length $max_sequence_length \
      --task $task \
      --bidirectional_rnn $bidirectional_rnn

cp ./model_hw3/test_results/intent.txt $2
