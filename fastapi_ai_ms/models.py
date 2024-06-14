""" PyDantic models """

from pydantic import BaseModel


# Create your models here.
class NLPModel(BaseModel):
    """Model for NLP"""

    text: str
