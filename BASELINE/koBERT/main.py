import json
import os

import torch
import argparse
import torch.nn as nn
from tqdm import trange
from transformers import XLMRobertaModel, AutoTokenizer
from torch.utils.data import DataLoader, TensorDataset
from transformers import get_linear_schedule_with_warmup
from transformers import AdamW
from datasets import load_metric
from sklearn.metrics import f1_score
import pandas as pd
import copy

import os
from sentiment_analysis import train_sentiment_analysis

import wandb
wandb.init(project="model_test")

train_sentiment_analysis()