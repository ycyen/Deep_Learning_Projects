#!/bin/bash

python3 my_eval.py --checkpoint_dir="./runs/1478963932/checkpoints/" --data_file="../data/dataset_cnn_eng/testing_data.txt"
#python3 my_eval.py --eval_train --checkpoint_dir="./runs/1478963932/checkpoints/" --data_file="../data/dataset_cnn_eng/training_data.neg" --positive_data_file="../data/dataset_cnn_eng/training_data.pos" --negative_data_file="../data/dataset_cnn_eng/training_data.neg"
