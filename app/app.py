from fastapi import FastAPI, File, UploadFile
from embeddings import get_embeddings
from vectorstore import VectorStore
import os

app = FastAPI()
VSTORE_PATH = os.getenv('VSTORE_PATH', './data/vstore')
vs = VectorStore(VSTORE_PATH)

@app.post('/upload')
async def upload_pdf(file: UploadFile = File(...)):
    data_dir = os.getenv('PDF_DATA_DIR','./data/pdfs')
    os.makedirs(data_dir, exist_ok=True)
    path = os.path.join(data_dir, file.filename)
    with open(path, 'wb') as f:
        f.write(await file.read())
    # Optionally call ingestion here
    return {'status':'ok','file':file.filename}

@app.get('/query')
def query(q:str):
    q_emb = get_embeddings([q])[0]
    results = vs.search(q_emb, k=5)
    return {'query': q, 'results': results}
