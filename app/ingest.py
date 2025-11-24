from utils import extract_text_from_pdf
from embeddings import get_embeddings
from vectorstore import VectorStore
from pathlib import Path
import os

DATA_DIR = Path(os.getenv("PDF_DATA_DIR", "./data/pdfs"))
VSTORE_PATH = Path(os.getenv("VSTORE_PATH", "./data/vstore"))

vs = VectorStore(str(VSTORE_PATH))

for pdf in DATA_DIR.glob("*.pdf"):
    text = extract_text_from_pdf(pdf)
    chunks = [c for c in text.split('\n\n') if len(c.strip()) > 50]
    emb = get_embeddings(chunks)
    vs.add_documents(doc_texts=chunks, embeddings=emb, metadata={"source": pdf.name})

vs.persist()
