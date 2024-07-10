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

    def pushr(self, key: str, value: str) -> int:
        return self.db.rpush(key, value)

    def pushl(self, key: str, value: str) -> int:
        return self.db.lpush(key, value)

    def popl(self, key: str) -> Optional[bytes]:
        return self.db.lpop(key)

    def delete(self, key: str) -> bool:
        return self.db.delete(key) == 1