from sentence_transformers import SentenceTransformer
from chunk import chunks
model = SentenceTransformer("BAAI/bge-small-en-v1.5")
embeddings = model.encode(chunks)
print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))