from pathlib import Path
from pypdf import PdfReader
from docx import Document
import pandas as pd
DATA_DIR = Path(r"C:\Users\verma\Downloads\enterprise_RAG\data")
def reading_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for i in reader.pages:
        text += i.extract_text() or ""

    return text

pdf_path = DATA_DIR / "Leave Policy Template.pdf"

pdf_text = reading_pdf(pdf_path)

print(pdf_text[:1000])

def reading_docx(file_path):
    document = Document(file_path)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text
docx_path = DATA_DIR / "employee_leave_notes.docx"

docx_text = reading_docx(docx_path)

print(docx_text[:1000])

def reading_csv(file_path):
    data = pd.read_csv(file_path)
    return data.to_string(index=False)
csv_path = DATA_DIR / "Employee Dataset - Full (1).csv"

csv_text = reading_csv(csv_path)

print(csv_text[:1000])
def reading_md(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text
md_path = DATA_DIR / "employee_faq.md"

md_text = reading_md(md_path)

print(md_text[:1000])
doc = [
    {
        "source": "Leave Policy Template.pdf",
        "type": "pdf",
        "text": pdf_text
    },
    {
        "source": "employee_leave_notes.docx",
        "type": "docx",
        "text": docx_text
    },
    {
        "source": "Employee Dataset - Full (1).csv",
        "type": "csv",
        "text": csv_text
    },
    {
        "source": "employee_faq.md",
        "type": "md",
        "text": md_text
    }
]
print("Total documents:", len(doc))