import sys
sys.stdout.reconfigure(encoding="utf-8")

from pathlib import Path
from pypdf import PdfReader
from docx import Document
import pandas as pd
from ingestion import doc
def fixed_chunking(text, chunk_size=100, overlap=20):

    words = text.split()
    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
chunks = fixed_chunking(doc[0]["text"])

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- CHUNK {i+1} ---")
    print(chunk)