""" PyDantic models """

from pydantic import BaseModel


# Create your models here.
class HFModel(BaseModel):
    """Adds model option to let the user to select which HF model to use."""

    model: str | None


class ChatCompletionModel(HFModel):
    """Chat completion model represents ChatCompletion input. Provides messages fields."""

    messages: list[dict[str, str]]


class QAModel(HFModel):
    """Question answering model represents QA input. Provides context and question fields."""

    context: str
    question: str


class SentenceSimilarityModel(HFModel):
    """Sentence similarity model represents SentenceSimilarity input. Provides sentence and sentences fields."""

    sentence: str
    sentences: list[str]


class PromptModel(HFModel):
    """Prompt model represents input for tasks that require a prompt. Provides prompt field."""

    prompt: str


class TextModel(HFModel):
    """Text model represents Text input. Provides text field"""

    text: str


class TranslationModel(TextModel):
    """Translation model represents Translation input. Provides source and target fields."""

    source: str
    target: str


class ZeroShotClassificationModel(TextModel):
    """Zero shot classification model represents ZeroShotClassification input. Provides labels and is_multi_label fields."""

    labels: list[str]
    is_multi_label: bool
