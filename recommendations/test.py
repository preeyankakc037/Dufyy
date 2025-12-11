# regenerate_embeddings.py
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
import os

# Paths
DATA_PATH = "data/test.csv"
EMB_PATH = "data/music_embeddings.pt"
BASE_DIR = os.path.dirname(__file__)

# Load data
print("Loading dataset...")
df = pd.read_csv(DATA_PATH)
print(f"Loaded {len(df)} songs")

# Combine text
texts = (
    df["music_name"].astype(str) + " by " +
    df["artist_name"].astype(str) + " genre " +
    df["genre"].astype(str)
).tolist()

print("Loading model (float32) → will convert to float16 after encoding...")
model = SentenceTransformer("all-MiniLM-L6-v2")   # ← normal loading

print("Encoding + converting to float16...")
embeddings = model.encode(
    texts,
    batch_size=64,
    show_progress_bar=True,
    convert_to_tensor=True,
    normalize_embeddings=True
)

# ← THIS IS THE ONLY LINE THAT ACTUALLY WORKS TODAY:
embeddings = embeddings.to(torch.float16)   # Convert AFTER encoding

torch.save(embeddings.cpu(), EMB_PATH)
size_mb = os.path.getsize(EMB_PATH) / (1024*1024)
print(f"Success! Saved float16 embeddings → {size_mb:.1f} MB")
print(f"Shape: {embeddings.shape} | dtype: {embeddings.dtype}")