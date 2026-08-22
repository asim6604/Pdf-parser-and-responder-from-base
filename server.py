from fastapi import FastAPI, UploadFile
from parsing import chunking
from pypdf import PdfReader
from embedding import embedding
from vector import Vector
from main import Api

import io

app=FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file:UploadFile):
    FileObject=await file.read();
   
    reader = PdfReader(io.BytesIO(FileObject))
    chunks=chunking(reader)
    Embed=embedding(chunks)
    Response=Vector(Embed,chunks)
    Reply=Api(Response)
    return{"Response":Reply}



 
