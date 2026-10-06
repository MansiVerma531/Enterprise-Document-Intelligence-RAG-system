
# Enterprise-Document-Intelligence-RAG
This project is a document-based question answering system using Retrieval-Augmented Generation (RAG).

The project works through the following steps:

1. **Document Ingestion**  
   The system accepts documents in different formats such as PDF, CSV, Markdown, and DOCX files and extracts their content.

2. **Structural Chunking**  
   The extracted content is divided into meaningful sections or chunks so that relevant information can be retrieved more effectively.

3. **Hybrid Search**  
   Hybrid search combines dense and sparse retrieval. Dense search finds information based on the meaning and context of the query, while sparse search focuses on important keywords and exact terms.

4. **Grounded Generation and Citations**  
   The retrieved information is provided to an LLM such as Llama to generate an answer based on the available documents. Citations are used to show the source of the information.

5. **Streamlit Interface**  
   A Streamlit-based user interface is used to allow users to ask questions and receive answers from the uploaded documents.
