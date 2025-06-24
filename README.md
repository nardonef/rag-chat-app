# 🏈 Fantasy Football League RAG Chat App

A Retrieval-Augmented Generation (RAG) application built with FastAPI that enables natural language querying over your data using LLMs and vector embeddings.

---

## ✨ Features

- ⚡ Ingests and indexes structured data (e.g., JSON exports)
- 🧠 Uses local or API-based embedding models (e.g., OpenAI, InstructorEmbedding, HuggingFace)
- 🧱 Stores vector indexes in a persistent or in-memory Chroma DB
- 🔁 Can be run on a cron job for periodic data ingestion
- 💬 FastAPI-based REST API for querying your data
- 🔧 Configurable and modular ingestion/query components

---

## Getting Started

### 1. Set Up the Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Set Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your-openai-key
```

### 3. Run the API

```bash
uvicorn api.main:app --reload
```

### 4. Ingest and Index Data

Run the ingestion script (can use api endpoint):

This loads all `.json` files from `/data`, creates document chunks, generates embeddings, and stores them in the Chroma vector DB.

### 5. Query

Query the application!

- Query endpoint: `GET /query?q=Who+are+the+top+waiver+pickups+this+week`


Access the app at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔌 Swappable Components

- **Vector Store**: Use in-memory or persistent Chroma
- **Index**: Load from documents or reuse stored index

---

## 🛠 Configuration

You can configure:

- Persistent vs. in-memory indexing
- Cron-compatible ingestion pipeline - TODO
- Logging, retry logic, and document pre-processing

---

## 📦 Requirements

- Python 3.12
- FastAPI
- ChromaDB
- LlamaIndex
- Open AI key
- Uvicorn
