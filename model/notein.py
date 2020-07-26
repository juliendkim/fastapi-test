from pydantic import BaseModel
from datetime import datetime


class NoteIn(BaseModel):
    content: str
    created: datetime
