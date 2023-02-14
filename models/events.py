from beanie import Document
from pydantic import BaseModel
from typing import List, Optional


class Event(Document):
    creator: Optional[str]
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Clean room",
                "image": "https:cleaning.ru/image.png",
                "description": "i will clean my room",
                "tags": ["python", "fastapi", "clean", "room"],
                "location": "Home"
            }
        }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Clean room",
                "image": "https:cleaning.ru/image.png",
                "description": "i will clean my room",
                "tags": ["python", "fastapi", "clean", "room"],
                "location": "Home"
            }
        }
