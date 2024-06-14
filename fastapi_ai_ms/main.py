""" FastAPI Microservice """

from fastapi import FastAPI
from huggingface_hub import InferenceClient


# App
app = FastAPI()

# HF Client
client = InferenceClient()


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint"""

    return {"details": "FastAPI AI microservice"}
