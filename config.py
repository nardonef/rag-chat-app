import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

USE_API_EMBEDDINGS = False
EMBEDDING_MODEL_NAME = "text-embedding-3-small"
CHROMA_DB_PATH = Path("./chroma_db")
CHROMA_COLLECTION_NAME = "jg_sleeper_data_v1"
DATA_DIR = Path("./data")
SLEEPER_USER_ID = "469959240648224768"
LEAGUE_YEAR = "2024"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise RuntimeError("Missing OPENAI_API_KEY env var")
