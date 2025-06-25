import logging
import sys
from fastapi import FastAPI
from pydantic import BaseModel
from ingestion.ingest import run_ingestion
from vector.query_engine import get_query_engine

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


app = FastAPI()


class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query_vector_store(request: QueryRequest):
    response = get_query_engine(request.question).query(
        request.question,
    )
    return {"response": str(response)}


@app.post("/ingest")
def ingest_sleeper(request: QueryRequest):
    run_ingestion()
    return {"response": str("Data ingestion completed successfully.")}
