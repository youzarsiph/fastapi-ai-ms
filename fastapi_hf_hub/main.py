""" FastAPI Microservice """

from pathlib import Path
from typing import Any
from fastapi import FastAPI
from fastapi.responses import FileResponse
from huggingface_hub import AsyncInferenceClient
from fastapi_hf_hub import models

# App
app = FastAPI()

# HF Client
client = AsyncInferenceClient()


@app.get("/")
async def root() -> dict[str, Any]:
    """Root endpoint"""

    return {"details": "FastAPI AI microservice"}


@app.post("/chat-completion")
async def chat_completion(request: models.ChatCompletionModel) -> dict[str, Any]:
    """A method for completing conversations using a specified language model."""

    return {
        "result": await client.chat_completion(
            messages=request.messages,
            model=request.model,
        )
    }


@app.post("/feature-extraction")
async def feature_extraction(request: models.TextModel) -> dict[str, Any]:
    """Generate embeddings for a given text."""

    return {
        "result": await client.feature_extraction(
            text=request.text,
            model=request.model,
        )
    }


@app.post("/fill-mask")
async def fill_mask(request: models.TextModel) -> dict[str, Any]:
    """Fill in a hole with a missing word (token to be precise)."""

    return {
        "result": await client.fill_mask(
            text=request.text,
            model=request.model,
        )
    }


@app.post("/question-answering")
async def question_answering(request: models.QAModel) -> dict[str, Any]:
    """Retrieve the answer to a question from a given text."""

    return {
        "answer": await client.question_answering(
            question=request.question,
            context=request.context,
            model=request.model,
        )
    }


@app.post("/sentence-similarity")
async def sentence_similarity(
    request: models.SentenceSimilarityModel,
) -> dict[str, Any]:
    """Compute the semantic similarity between a sentence and a list of other sentences by comparing their embeddings."""

    return {
        "result": await client.sentence_similarity(
            sentence=request.sentence,
            other_sentences=request.sentences,
            model=request.model,
        )
    }


@app.post("/summarization")
async def summarization(request: models.TextModel) -> dict[str, Any]:
    """Generate a summary of a given text using a specified model."""

    return {
        "summary": await client.summarization(
            text=request.text,
            model=request.model,
        )
    }


@app.post("/text-classification")
async def text_classification(request: models.TextModel) -> dict[str, Any]:
    """Perform text classification (e.g. sentiment-analysis) on the given text."""

    return {
        "result": await client.text_classification(
            text=request.text,
            model=request.model,
        )
    }


@app.post("/text-generation")
async def text_generation(request: models.PromptModel) -> dict[str, Any]:
    """Given a prompt, generate the following text."""

    return {
        "result": await client.text_generation(
            prompt=request.prompt,
            model=request.model,
        )
    }


@app.post("/text-to-image")
async def text_to_image(request: models.PromptModel) -> FileResponse:
    """Generate an image based on a given text using a specified model."""

    image = await client.text_to_image(
        prompt=request.prompt,
        model=request.model,
    )
    image.save("image.png")

    return FileResponse("image.png")


@app.post("/text-to-speech")
async def text_to_speech(request: models.TextModel) -> FileResponse:
    """Synthesize an audio of a voice pronouncing a given text."""

    audio = await client.text_to_speech(
        text=request.text,
        model=request.model,
    )
    Path("audio.flac").write_bytes(audio)

    return FileResponse("audio.flac")


@app.post("/token-classification")
async def token_classification(request: models.TextModel) -> dict[str, Any]:
    """
    Perform token classification on the given text. Usually used for sentence parsing, either grammatical,
    or Named Entity Recognition (NER) to understand keywords contained within text.
    """

    return {
        "result": await client.token_classification(
            text=request.text,
            model=request.model,
        )
    }


@app.post("/translation")
async def translation(request: models.TranslationModel) -> dict[str, Any]:
    """Convert text from one language to another."""

    return {
        "translation": await client.translation(
            text=request.text,
            model=request.model,
            src_lang=request.source,
            tgt_lang=request.target,
        )
    }


@app.post("/zero-shot-classification")
async def zero_shot_classification(
    request: models.ZeroShotClassificationModel,
) -> dict[str, Any]:
    """Provide as input a text and a set of candidate labels to classify the input text."""

    return {
        "result": await client.zero_shot_classification(
            text=request.text,
            labels=request.labels,
            multi_label=request.is_multi_label,
            model=request.model,
        )
    }
