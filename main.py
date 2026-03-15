from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2", "prompt": request.prompt, "stream": False},
    )

    data = response.json()

    return {"response": data["response"]}
