import faiss
import numpy as np
import pickle
import os

class VectorStore:
    def __init__(self, path):
        self.path = path
        os.makedirs(path, exist_ok=True)
        self.index_path = os.path.join(path, 'faiss.index')
        self.meta_path = os.path.join(path, 'meta.pkl')
        self.index = None
        self.metadata = []
        self._load()

    def _load(self):
        if os.path.exists(self.index_path) and os.path.exists(self.meta_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.meta_path, 'rb') as f:
                self.metadata = pickle.load(f)
        else:
            self.index = None
            self.metadata = []

    def add_documents(self, doc_texts, embeddings, metadata=None):
        emb_array = np.array(embeddings).astype('float32')
        if self.index is None:
            d = emb_array.shape[1]
            self.index = faiss.IndexFlatL2(d)
        self.index.add(emb_array)
        for i, t in enumerate(doc_texts):
            md = metadata.copy() if metadata else {}
            md.update({"text": t})
            self.metadata.append(md)

    def search(self, q_emb, k=5):
        q = q_emb.astype('float32')
        D, I = self.index.search(q.reshape(1, -1), k)
        return [self.metadata[idx] for idx in I[0]]

    def persist(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, 'wb') as f:
            pickle.dump(self.metadata, f)
