from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None  # reserved for future multi-turn memory


class ChatResponse(BaseModel):
    answer: str
    session_id: Optional[str] = None