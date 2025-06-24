from vector.vector_store import get_vector_store
from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.vector_stores import MetadataFilters, ExactMatchFilter
from vector.preprocessing import extract_metadata_filters


def get_query_engine(query: str) -> RetrieverQueryEngine:
    """Returns a query engine with a dynamic filter based on the user query."""

    filters = build_filters(query)
    vector_store = get_vector_store()
    index = VectorStoreIndex.from_vector_store(vector_store)
    retriever = index.as_retriever(filters=filters, similarity_top_k=3)
    return RetrieverQueryEngine(retriever=retriever)


def build_filters(query: str) -> MetadataFilters:
    """Builds metadata filters based on the query."""

    metadata_filters = extract_metadata_filters(query)
    print(f"Extracted metadata_filters from query: {metadata_filters}")
    doc_type = metadata_filters.get("type")
    
    if doc_type:
        return MetadataFilters(
            filters=[ExactMatchFilter(key="type", value=doc_type)],
        )
    return None
