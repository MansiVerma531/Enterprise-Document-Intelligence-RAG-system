import faiss
from embeddings import embeddings
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
print("Number of vectors:", index.ntotal)