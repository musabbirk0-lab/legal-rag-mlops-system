import os
USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == 'true'

if USE_OPENAI:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    def get_embeddings(texts):
        res = openai.Embedding.create(model="text-embedding-3-small", input=texts)
        return [r['embedding'] for r in res['data']]
else:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    def get_embeddings(texts):
        return model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
