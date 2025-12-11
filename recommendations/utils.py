# recommendations/utils.py
import logging
import numpy as np
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
from django.conf import settings
from pathlib import Path

logger = logging.getLogger(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

def fix_typo(query: str) -> str:
    corrections = {
        "paino": "piano", "pianno": "piano", "painoo": "piano",
        "fashon": "fashion", "fassion": "fashion", "fashin": "fashion",
        "comdey": "comedy", "comdy": "comedy", "commedy": "comedy",
        "reals": "reels", "reelz": "reels", "rels": "reels",
        "lofi": "lofi", "lo-fi": "lofi", "lowfi": "lofi",
        "studey": "study", "studi": "study"
    }
    return " ".join(corrections.get(w, w) for w in query.lower().split())

def recommend_similar_songs(query: str, top_k: int = 10):
    query = fix_typo(query)
    data_dir = Path(settings.BASE_DIR) / "recommendations" / "data"
    
    index_path = data_dir / "faiss_index.index"
    embeddings_path = data_dir / "embeddings.npy"
    csv_path = data_dir / "preprocessed_music_dataset.csv"

    if not all(p.exists() for p in [index_path, embeddings_path, csv_path]):
        logger.error("FAISS files missing!")
        return []

    try:
        index = faiss.read_index(str(index_path))
        df = pd.read_csv(csv_path, encoding='utf-8')
        query_vec = model.encode([query]).astype('float32')
        faiss.normalize_L2(query_vec)
        scores, indices = index.search(query_vec, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx >= len(df): continue
            row = df.iloc[idx]
            results.append({
                "music_name": str(row["music_name"]),
                "artist_name": str(row["artist_name"]),
                "music_link": str(row["music_link"]),
                "image_url": str(row.get("image_url", "https://via.placeholder.com/300")),
                "similarity": round(float(score), 3)
            })
        logger.info(f"Search '{query}' -> {len(results)} results")
        return results
    except Exception as e:
        logger.error(f"FAISS error: {e}")
        return []