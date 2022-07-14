from motor.motor_asyncio import AsyncIOMotorClient as _async_IO_motor_client
from beanie import init_beanie
from core.config import settings
from db.models.user import UserHistory


async def initiate_database():
    client = _async_IO_motor_client(settings.MONGODB_URL)
    await init_beanie(
        database=client.get_default_database(), document_models=[UserHistory]
    )

