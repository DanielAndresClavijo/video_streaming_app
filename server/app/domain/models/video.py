from pydantic import BaseModel
from typing import Any, Optional

class Video(BaseModel):
    id: Optional[int]
    user_id: str
    title: str
    description: str
    url: str
    created_at: Optional[str] = ''
    updated_at: Optional[str] = ''


    def model_dump(self) ->  dict[str, Any]:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

class UpdateVideoRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    updated_at: Optional[str] = None


    def model_dump(self) ->  dict[str, Any]:
        return {
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'updated_at': self.updated_at,
        }