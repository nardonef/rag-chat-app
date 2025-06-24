# import os
# from llama_index.readers.json import JSONReader
import json
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from vector.vector_store import get_vector_store, get_embedding_model
from ingestion.sleeper.data_transformers import chunk_leagues, chunk_rosters, chunk_players
from config import DATA_DIR

FILES = ["leagues.json", "players.json", "roster.json"]

def get_documents(directory=DATA_DIR):
    """Load and transform data from JSON files into documents."""
    # documents = []
    # reader = JSONReader()
    # for file in os.listdir(directory):
    #     if file.endswith(".json"):
    #         docs = reader.load_data(directory / file)
    #         documents.extend(docs)

    with open(directory / "leagues.json", "r") as leagues_file:
        leagues = json.load(leagues_file)

    with open(directory / "players.json", "r") as players_file:
        players = json.load(players_file)

    with open(directory / "rosters.json", "r") as rosters_file:
        rosters = json.load(rosters_file)

    documents = chunk_leagues(leagues) + chunk_rosters(rosters) + chunk_players(players)

    return documents


def run_ingestion():
    """Ingests data into the vector store."""
    documents = get_documents(DATA_DIR)
    vector_store = get_vector_store()
    embed_model = get_embedding_model()
    Settings.embed_model = embed_model

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    VectorStoreIndex.from_documents(documents, storage_context=storage_context)

    print(f"Ingested {len(documents)} documents into vector store.")


if __name__ == "__main__":
    run_ingestion()
