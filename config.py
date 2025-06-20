import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # loads from .env into os.environ

USE_API_EMBEDDINGS = False
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # or openai ada
CHROMA_DB_PATH = Path("./chroma_db")
CHROMA_COLLECTION_NAME = "jg_sleeper_data_v1"
DATA_DIR = Path("./data")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise RuntimeError("Missing OPENAI_API_KEY env var")
