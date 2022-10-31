#!/bin/bash
python sentiment_analysis.py \
  --test_data /home/nlplab/Devlopment/2022_korean_AI/ajin/ABSA_ensemble_test/data/nikluge-sa-2022-test.jsonl \
  --base_model monologg/koelectra-small-v2-discriminator \
  --do_test \
  --entity_property_model_path ../saved_model/category_extraction/saved_model_epoch_8.pt \
  --polarity_model_path ../saved_model/polarity_classification/saved_model_epoch_10.pt \
  --batch_size 8 \
  --max_len 256