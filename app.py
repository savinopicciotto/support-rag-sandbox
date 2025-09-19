from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Support RAG Sandbox")

class AskIn(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ask")
def ask(body: AskIn):
    # Placeholder response; wire your retrieval logic here.
    return {"answer": f"Stub answer for: {body.query}", "citations": ["doc://example"]}