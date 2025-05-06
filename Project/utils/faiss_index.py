import faiss
import numpy as np
from utils.embedder import get_embeddings
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))
    return index

def search_faiss_index(query, chunks, embeddings, index, top_k=3):
    query_embedding = get_embeddings([query])[0]
    query_vector = np.array([query_embedding]).astype('float32')
    _, I = index.search(query_vector, top_k)
    return [chunks[i] for i in I[0]]
