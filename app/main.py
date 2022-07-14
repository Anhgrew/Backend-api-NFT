# from functools import lru_cache
from fastapi import FastAPI
from core.config import settings
from db.db import initiate_database
from routes.user import router as UserRouter

app = FastAPI()


@app.on_event("startup")
async def start_database():
    await initiate_database()


app.include_router(UserRouter, prefix="/users")
