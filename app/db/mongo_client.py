# MongoDB connection logic
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import Settings

settings = Settings()

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]
