#!/bin/bash

python3 sentiment_analysis.py \
  --train_data /home/nlplab/Devlopment/2022_korean_AI/ajin/ABSA_ensemble_test/data/nikluge-sa-2022-train.jsonl \
  --dev_data /home/nlplab/Devlopment/2022_korean_AI/ajin/ABSA_ensemble_test/data/nikluge-sa-2022-dev.jsonl \
  --base_model monologg/koelectra-small-v2-discriminator \
  --do_train \
  --do_eval \
  --learning_rate 3e-6 \
  --eps 1e-8 \
  --num_train_epochs 20 \
  --entity_property_model_path ../saved_model/category_extraction/ \
  --polarity_model_path ../saved_model/polarity_classification/ \
  --batch_size 8 \
  --max_len 256