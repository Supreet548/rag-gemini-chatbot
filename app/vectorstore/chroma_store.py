import os
from dotenv import load_dotenv
from langchain_chroma import Chroma

load_dotenv()

def create_vectorstore(chunks, embeddings):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=os.getenv("CHROMA_DB")
    )

    return vector_store