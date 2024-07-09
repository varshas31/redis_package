import redis
from typing import Optional

class RedisClient:
    def __init__(self, config: dict):
        self.db = redis.Redis(
            host=config['host'],
            port=config['port'],
            db=config['db'],
            password=config.get('password')
        )

    def push(self, key: str, value: str) -> int:
        """Pushes a value to a list in Redis."""
        return self.db.lpush(key, value)

    def pop_left(self, key: str) -> Optional[bytes]:
        """Pops a value from the head of a list in Redis."""
        return self.db.lpop(key)

    def pop_right(self, key: str) -> Optional[bytes]:
        """Pops a value from the tail of a list in Redis (FIFO for Queue)."""
        return self.db.rpop(key)
