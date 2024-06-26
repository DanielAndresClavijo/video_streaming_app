from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[int]
    email: EmailStr
    hashed_password: str

    def model_dump(self):
        return self.dict()

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    def model_dump(self):
        return self.dict()
