# RAG Chatbot with Gemini and ChromaDB

A simple Retrieval-Augmented Generation (RAG) chatbot built using LangChain, Google Gemini, Google Embeddings, and ChromaDB.

The application supports question answering from both PDF documents and web pages by retrieving relevant context before generating responses.

---

## Features

* PDF document ingestion using PyPDFLoader
* Website ingestion using WebBaseLoader
* Text chunking with RecursiveCharacterTextSplitter
* Semantic search using ChromaDB
* Google Generative AI Embeddings
* Gemini 2.5 Flash LLM
* Context-aware question answering
* Modular project structure
* Environment variable based configuration

---

## Architecture

User Query
↓
Document Loader (PDF / Website)
↓
Text Splitting
↓
Google Embeddings
↓
ChromaDB Vector Store
↓
Retriever
↓
Gemini 2.5 Flash
↓
Generated Answer

---

## Project Structure

```text
RAG/
│
├── app/
│   ├── loaders/
│   │   ├── pdf_loader.py
│   │   └── web_loader.py
│   │
│   ├── embeddings/
│   │   └── embedding_service.py
│   │
│   ├── llms/
│   │   └── gemini_llm.py
│   │
│   ├── vectorstore/
│   │   └── chroma_store.py
│   │
│   └── main.py
│
├── data/
├── chroma_db/
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Supreet548/rag-gemini-chatbot.git
cd rag-gemini-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY

MODEL_CHAT=gemini-2.5-flash

MODEL_EMBED=models/embedding-001

CHROMA_DB=chroma_db
```

---

## Running the Application

```bash
python -m app.main
```

Select the data source:

```text
1. PDF
2. Website
```

### PDF Example

```text
Enter Choice: 1

Enter PDF Path:
data/Art11.pdf

Ask Question:
What is adolescence?
```

### Website Example

```text
Enter Choice: 2

Enter Website URL:
https://en.wikipedia.org/wiki/Artificial_intelligence
```

---

## Tech Stack

* Python
* LangChain
* Google Gemini 2.5 Flash
* Google Generative AI Embeddings
* ChromaDB
* PyPDF
* WebBaseLoader

---

## Future Improvements

* FastAPI Integration
* Conversation Memory
* Hybrid Search
* Reranking
* RAG Evaluation
* Docker Support
* CI/CD Pipeline

---

## Author

Supreet Kumar

Generative AI Engineer

 