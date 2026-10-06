import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from pypdf import PdfReader
from docx import Document
import pandas as pd
from ingestion import doc
def spliting(text):
    sections=text.split("\n")
    chunks=[]
    for i in sections:
       if i.strip():
           chunks.append(i.strip())
    return chunks
chunks=spliting(doc[0]["text"])
print("Total chunks",len(chunks))
print(repr(doc[0]["text"][:1000]))
for i, d in enumerate(doc):
    print("\nDOCUMENT", i + 1)
    print(d["text"][:1500])

def structural_chunking(text):

    lines = text.split("\n")
    chunks = []
    current_chunk = []
    title = ""

    for line in lines:

        if line.startswith("# "):
            title = line

        elif line.startswith("## "):

            if current_chunk:
                chunks.append("\n".join(current_chunk).strip())

            current_chunk = [title, line]

        elif line.strip():
            current_chunk.append(line)

    if current_chunk:
        chunks.append("\n".join(current_chunk).strip())

    return chunks
chunks = structural_chunking(doc[3]["text"])

print("Total structural chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- CHUNK {i+1} ---")
    print(chunk)