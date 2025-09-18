# Redis caching logic
import aioredis
from app.config.settings import settings

class RedisClient:
    def __init__(self):
        self.redis = None

    async def init(self):
        self.redis = await aioredis.from_url(
            f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
            encoding="utf-8",
            decode_responses=True
        )

    async def get(self, key: str):
        if self.redis:
            return await self.redis.get(key)

    async def set(self, key: str, value: str, expire: int = 60):
        if self.redis:
            await self.redis.set(key, value, ex=expire)

cache = RedisClient()
