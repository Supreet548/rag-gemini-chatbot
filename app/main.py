from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate

from app.loaders.pdf_loader import load_pdf
from app.loaders.web_loader import load_web

from app.embeddings.embedding_service import embeddings
from app.llms.gemini_llm import llm

from app.vectorstore.chroma_store import create_vectorstore

from dotenv import load_dotenv

load_dotenv()

choice = input("""
1. PDF
2. Website

Enter Choice:
""")


if choice == "1":

    path = input(
        "Enter PDF Path (example: data/Art11.pdf): "
    )

    docs = load_pdf(path)

elif choice == "2":

    url = input(
        "Enter Website URL: "
    )

    docs = load_web(url)

else:

    print("Invalid Choice")
    exit()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

vector_store = create_vectorstore(
    chunks,
    embeddings
)


retriever = vector_store.as_retriever(
    search_kwargs={"k":2}
)


question = input("\nAsk Question: ")


retrieved_docs = retriever.invoke(question)


context = "\n\n".join(
    doc.page_content
    for doc in retrieved_docs
)


prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Answer ONLY from the provided context.

If context is insufficient,
say "I don't know."

Context:
{context}

Question:
{question}
""",
    input_variables=[
        "context",
        "question"
    ]
)


final_prompt = prompt.invoke(
    {
        "context": context,
        "question": question
    }
)


response = llm.invoke(final_prompt)

print("\nAnswer:\n")

print(response.content)