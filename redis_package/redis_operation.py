import redis
from .config import redis_config

class RedisClient:
    def __init__(self, config=None):
        self.db = redis.Redis(**(config or redis_config))

    def push(self, key: str, value: str) -> int:
        if not self.is_list(key):
            self.db.delete(key)  # Remove key if it's not a list
        return self.db.lpush(key, value)

    def pop(self, key: str) -> str:
        if not self.is_list(key):
            return None
        return self.db.lpop(key)

    def get_all(self, key: str) -> list:
        if not self.is_list(key):
            return []
        return self.db.lrange(key, 0, -1)

    def get_all_keys(self) -> list:
        return self.db.keys('*')

    def remove(self, key: str, value: str) -> int:
        if not self.is_list(key):
            return 0
        return self.db.lrem(key, 0, value)

    def update(self, key: str, index: int, value: str) -> bool:
        if not self.is_list(key):
            return False
        try:
            self.db.lset(key, index, value)
            return True
        except redis.exceptions.ResponseError:
            return False

    def len(self, key: str) -> int:
        if not self.is_list(key):
            return 0
        return self.db.llen(key)

    def is_list(self, key: str) -> bool:
        if self.db.exists(key):
            return self.db.type(key) == b'list'
        return True
