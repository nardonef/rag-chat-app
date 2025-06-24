import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from config import CHROMA_DB_PATH, CHROMA_COLLECTION_NAME, EMBEDDING_MODEL_NAME


def get_vector_store():
    """Returns a Chroma vector store instance."""
    chroma_client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
    collection = chroma_client.get_or_create_collection(CHROMA_COLLECTION_NAME)
    return ChromaVectorStore(chroma_collection=collection)


def get_embedding_model():
    """Returns an OpenAI embedding model instance."""
    return OpenAIEmbedding(model=EMBEDDING_MODEL_NAME)
