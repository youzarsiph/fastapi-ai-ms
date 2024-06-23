""" PyDantic models """

from pydantic import BaseModel


# Create your models here.
class HFModel(BaseModel):
    """Adds model option to let the user to select which HF model to use"""

    model: str | None


class ChatCompletionModel(HFModel):
    """Chat completion model"""

    messages: list[dict[str, str]]


class QAModel(HFModel):
    """Question answering model"""

    context: str
    question: str


class SentenceSimilarityModel(HFModel):
    """Sentence similarity model"""

    sentence: str
    sentences: list[str]


class PromptModel(HFModel):
    """Prompt model"""

    prompt: str


class TextModel(HFModel):
    """Text model"""

    text: str


class TranslationModel(TextModel):
    """Translation model"""

    source: str
    target: str


class ZeroShotClassificationModel(TextModel):
    """Translation model"""

    labels: list[str]
    is_multi_label: bool
