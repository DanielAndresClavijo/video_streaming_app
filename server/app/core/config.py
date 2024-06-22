import os
from supabase import create_client, Client

class Config:
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')

def init_supabase() -> Client:
    return create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
