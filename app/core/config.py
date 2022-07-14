from pydantic import BaseSettings
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
# env_path = Path(".") / ".env"


class Settings(BaseSettings):
    app_name: str = "User Api"
    MONGODB_URL = os.getenv("MONGODB_URL")
    ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
    SECRET_ACCESS_ID = os.getenv("SECRET_ACCESS_ID")
    SEARCH_API = os.getenv("SEARCH_API")
    # class Config:
    #     env_file = env_path


settings = Settings()
