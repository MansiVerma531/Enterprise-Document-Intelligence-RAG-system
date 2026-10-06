from rank_bm25 import BM25Okapi
from chunk import chunks
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