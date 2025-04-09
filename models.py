from beanie import Document
from pydantic import BaseModel


class PredictionModel(Document):
    image_id: str
    image: str
    confidence: float


class PredictionRequest(BaseModel):
    file: bytes

