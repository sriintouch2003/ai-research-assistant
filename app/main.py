import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel, Field

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from app.services.openai_service import summarize_text
from app.services.serper_service import search
from app.services.langchain_agent_service import agent

app = FastAPI()

class Query(BaseModel):
    query: str

class SummarizationRequest(BaseModel):
    prompt: str
    query: str

@app.get("/")
def home():
    return {"message": "Welcome to the AI Research API"}

@app.post("/openai/")
def openai_endpoint(request: SummarizationRequest):
    result = summarize_text(request.prompt, request.query)
    return {"response": result}

@app.get("/serper/")
def serper_endpoint(query: Query):
    query = query.query
    result = search(query)
    return {"results": result}

@app.post("/research")
def researchAgent(query: Query):
    query = query.query
    content = agent({"input": query})
    actual_content = content["output"]
    return actual_content