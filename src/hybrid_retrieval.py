from rank_bm25 import BM25Okapi
from chunk import chunks
from vector_store import index
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("BAAI/bge-small-en-v1.5")
tokenized_chunks = [chunk.lower().split() for chunk in chunks]
bm25 = BM25Okapi(tokenized_chunks)
query = "How can I apply for planned leave?"
tokenized_query = query.lower().split()
scores = bm25.get_scores(tokenized_query)
print(scores)
top_k=3
top_indices = scores.argsort()[-top_k:][::-1]
print(top_indices)
top_chunks = [chunks[i] for i in top_indices]
for i in top_indices:
    print(f"\n--- RETRIEVED CHUNK{i+1} ---")
    print(chunks[i])
query_embedding = model.encode([query])
top_k = 3
distances, indices = index.search(query_embedding, top_k)
print("Faiss distances:",distances)
print("Faiss indices:",indices)
combined_scores = {}
for rank, i in enumerate(top_indices):
    combined_scores[i] = combined_scores.get(i, 0) + (top_k - rank)

for rank, i in enumerate(indices[0]):
    combined_scores[i] = combined_scores.get(i, 0) + (top_k - rank)
final_indices = sorted(combined_scores, key=combined_scores.get, reverse=True)
final_indices = final_indices[:3]
for i in final_indices:
    print(f"\n--- HYBRID CHUNK {i+1} | SCORE {combined_scores[i]} ---")
    print(chunks[i])