import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    VIDEO_DIRECTORY = os.getenv('/video_files')
    SUPABASE_VIDEOS_BUCKET_ID = os.getenv('SUPABASE_VIDEOS_BUCKET_ID')
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    JWT_SECRET = os.getenv('JWT_SECRET')

def init_supabase() -> Client:
    return create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
 