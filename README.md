# RAG Chatbot with Gemini and ChromaDB

A Retrieval-Augmented Generation (RAG) chatbot built using LangChain, Gemini 2.5 Flash, Google Embeddings, and ChromaDB.

## Features

* PDF Document Loading
* Website Loading using WebBaseLoader
* Semantic Search with ChromaDB
* Google Gemini 2.5 Flash
* Google Embeddings
* Modular Project Structure
* Environment Variable Configuration

## Tech Stack

* Python
* LangChain
* Google Gemini
* ChromaDB
* PyPDF
* WebBaseLoader

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
MODEL_CHAT=gemini-2.5-flash
MODEL_EMBED=models/embedding-001
CHROMA_DB=chroma_db
```

Run:

```bash
python -m app.main
```

## Project Structure

app/

* loaders/
* embeddings/
* llms/
* vectorstore/
* main.py

## Future Enhancements

* FastAPI Integration
* Conversation Memory
* Hybrid Search
* Reranking
* RAG Evaluation
* Docker Support
 