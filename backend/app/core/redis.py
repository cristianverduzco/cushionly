import redis
from app.core.config import settings

# Connect to Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True  # So it returns strings not bytes
)
