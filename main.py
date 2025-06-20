from fastapi import FastAPI
from pydantic import BaseModel
from ingestion.ingest import run_ingestion
from vector.query_engine import get_query_engine

app = FastAPI()


class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query_vector_store(request: QueryRequest):
    response = get_query_engine().query(request.question)
    return {"response": str(response)}


@app.post("/ingest")
def ingest_sleeper(request: QueryRequest):
    run_ingestion()
    return {"response": str("Data ingestion completed successfully.")}
