from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from passlib.context import CryptContext
from app.domain.models.user import UserCreate, User
from app.core.config import init_supabase

router = APIRouter()
supabase = init_supabase()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=User)
def register(user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.model_dump()
    user_dict['hashed_password'] = hashed_password
    del user_dict['password']
    response = supabase.table('users').insert(user_dict).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return User(**response.data[0])

@router.post("/login")
def login(user: UserCreate, Authorize: AuthJWT = Depends()):
    response = supabase.table('users').select('*').eq('email', user.email).execute()
    if response.error or not response.data:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    db_user = response.data[0]
    if not pwd_context.verify(user.password, db_user['hashed_password']):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    access_token = Authorize.create_access_token(subject=db_user['id'])
    return {"access_token": access_token}
