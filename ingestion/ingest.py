import os
from llama_index.readers.json import JSONReader
from llama_index.core import VectorStoreIndex, StorageContext
from vector.vector_store import get_vector_store
from config import DATA_DIR


def run_ingestion():
    documents = []
    reader = JSONReader()

    for file in os.listdir(DATA_DIR):
        if file.endswith(".json"):
            docs = reader.load_data(DATA_DIR / file)
            documents.extend(docs)

    vector_store = get_vector_store()
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )

    print(f"Ingested {len(documents)} documents into vector store.")


if __name__ == "__main__":
    run_ingestion()
