from vector.vector_store import get_vector_store
from llama_index.core import VectorStoreIndex

def get_query_engine():
    vector_store = get_vector_store()
    index = VectorStoreIndex.from_vector_store(
        vector_store
    )
    return index.as_query_engine()
