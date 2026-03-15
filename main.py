from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


@app.get("/health")
def health():
    return {"status": "Ok"}


@app.post("/chat")
def chat(requests: ChatRequest):
    return {"prompt": requests.prompt}
