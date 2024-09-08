from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from core.settings import settings


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    try:
        redis = aioredis.from_url(
            f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"
        )
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
        yield
    except Exception:
        yield
    finally:
        await redis.aclose()
