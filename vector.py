import chromadb
import uuid
from parsing import chunking
from embedding import embedding
import hashlib
def Vector(embeddings,chunks):
    chroma_client = chromadb.Client()
    file_hash = hashlib.sha256(embeddings).hexdigest()
    collection = chroma_client.get_or_create_collection(name="file_hash")
    dir(chroma_client)
    List_embed=embeddings.tolist();

   
    length=len(chunks)
    id=[]
    for i in range(0,length,1):
        n=str(i)
        id.append(n)
    collection.add(ids=id,
    documents=chunks,
    embeddings=List_embed
    ) 


    results =collection.query(
    query_texts=["what is shape of the earth"],
    n_results=2)

    complete="\n".join(results['documents'][0])

    return complete
