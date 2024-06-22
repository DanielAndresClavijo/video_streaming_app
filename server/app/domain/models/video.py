from pydantic import BaseModel
from typing import Optional

class Video(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    url: str
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True
