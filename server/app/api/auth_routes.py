from passlib.context import CryptContext
from fastapi import APIRouter, HTTPException
from app.domain.models.user import UserCreate, User
from app.core.config import init_supabase
from gotrue.errors import AuthApiError

router = APIRouter()
supabase = init_supabase()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=User)
def register(user: UserCreate):
    try:
        hashed_password = pwd_context.hash(user.password)
        response = supabase.auth.sign_up({
            'email': user.email,
            'password': hashed_password,
        })
        
        return {"access_token": response.get("access_token")}
    except Exception as err:
        raise HTTPException(status_code=400, detail=err.__dict__)

@router.post("/login")
def login(user: UserCreate):
    try:
        print("Hello world 0")
        # hashed_password = pwd_context.hash(user.password)
        print("Hello world 1 {}".format(user.password))
        response = supabase.auth.sign_in_with_password({
            'email': user.email,
            'password': user.password,
        })
        print("Hello world 2")
        print(response)
        
        
        return {"access_token": response.session.access_token}
    except AuthApiError as err:
        print("#########################")
        print(err.name)
        print(err.message)
        print(err.status)
        print(err.args)
        print(err.to_dict())
        print(err.to_dict())
        print("#########################")
        raise HTTPException(status_code=err.status, detail=err.__dict__)
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=err.__dict__)

@router.get("/sign_out")
def sign_out():
  res = supabase.auth.sign_out()
  return "success"
