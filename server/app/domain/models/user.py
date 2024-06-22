from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[int]
    email: EmailStr
    hashed_password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
