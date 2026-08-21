from sentence_transformers import SentenceTransformer
from parsing  import chunking
model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2");
def embedding():
    chunks=chunking();
    embeddings=model.encode(chunks);
    return embeddings;





