import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Setting(BaseSettings):
    GOOGLE_TOKEN_ENDPOINT: str = "https://oauth2.googleapis.com/token"
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
    REDIRECT_URI: str = "http://localhost:8000/auth/google"
    MONGO_DB_URI: str = os.getenv("MONGO_DB_URI")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    ALGORITHM: str = "HS256"
    JWT_TOKEN_EXPIRE_MINUTES: int = 43200
    UPLOAD_DIR: str = os.getenv("UPLOAD_PATH")


setting = Setting()
