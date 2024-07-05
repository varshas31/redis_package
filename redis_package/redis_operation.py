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
        if not self.is_list(key):
            self.db.delete(key)  # Remove key if it's not a list
        return self.db.lpush(key, value)

    def pop(self, key: str) -> Optional[bytes]:
        """Pops a value from the head of a list in Redis."""
        return self.db.lpop(key)

    def is_list(self, key: str) -> bool:
        """Checks if a key exists and is a list."""
        return self.db.exists(key) and self.db.type(key) == b'list'
