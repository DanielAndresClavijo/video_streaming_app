from pydantic import BaseModel
from typing import Optional

class Video(BaseModel):
    id: Optional[int]
    user_id: str
    title: str
    description: str
    url: str
    created_at: Optional[str] = ''
    updated_at: Optional[str] = ''


    def model_dump(self):
        return self.dict()
