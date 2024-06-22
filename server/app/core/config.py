import os
from dotenv import load_dotenv
from supabase import create_client, Client
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseSettings

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Settings(BaseSettings):
    authjwt_secret_key: str = os.getenv('JWT_SECRET_KEY')

class Config:
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    
@AuthJWT.load_config
def get_config():
    return Settings()

def init_supabase() -> Client:
    return create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
