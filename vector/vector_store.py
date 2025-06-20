import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from config import CHROMA_DB_PATH, CHROMA_COLLECTION_NAME


def get_vector_store():
    chroma_client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
    collection = chroma_client.get_or_create_collection(CHROMA_COLLECTION_NAME)
    return ChromaVectorStore(chroma_collection=collection)
