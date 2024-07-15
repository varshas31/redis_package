import redis
from redis_package.config import redis_config

class RedisClient:
    def __init__(self, config: dict):
        self.db = redis.Redis(
            host=config['host'],
            port=config['port'],
            db=config['db'],
        )

# Initialize Redis client
client = RedisClient(redis_config)

class Queue:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, value: str) -> int:
        try:
            return self.client.db.rpush(self.name, value)
        except Exception as e:
            return e

    def read(self) -> [bytes]:
        try:
            return self.client.db.lpop(self.name)
        except Exception as e:
            return e

    def delete(self) -> bool:
        try:
            return self.client.db.delete(self.name) == 1
        except Exception as e:
            return e

class Stack:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, value: str) -> int:
        try:
            return self.client.db.lpush(self.name, value)
        except Exception as e:
            return e

    def read(self) -> [bytes]:
        try:
            return self.client.db.lpop(self.name)
        except Exception as e:
            return e

    def delete(self) -> bool:
        try:
            return self.client.db.delete(self.name) == 1
        except Exception as e:
            return e
