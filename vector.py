import chromadb
from parsing import chunking
from embedding import embedding
def Vector():
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection")
    embeddings=embedding();
    List_embed=embeddings.tolist();

    chunks=chunking();
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
