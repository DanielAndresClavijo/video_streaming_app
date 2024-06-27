from pydantic import BaseModel, EmailStr
from typing import Optional
from gotrue import User as BaseUser

class User(BaseModel):
    id: Optional[str]
    email: EmailStr
    hashed_password: str

    def model_dump(self):
        return {
            'id': self.id,
            'email': self.email,
            'hashed_password': self.hashed_password,
        }
    
    @staticmethod
    def from_base_user(baseUser=BaseUser):
        return User(
            id= baseUser.id,
            email=  baseUser.email,
            hashed_password= ""
        )

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
    def model_dump(self):
        return {
            'email': self.email,
            'hashed_password': self.password,
        }
