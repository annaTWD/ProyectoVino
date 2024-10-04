import pandas as pd
import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch

df = pd.read_csv('../data/skills.csv', sep=';')

