from redis_package.config import redis_config
import redis
class RedisClient:
    def __init__(self, config: dict):
        self.db = redis.Redis(
            host=config['host'],
            port=config['port'],
            db=config['db'],
            password=config.get('password')
        )

# Initialize Redis client
client = RedisClient(config=redis_config)

class Queue:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, value: str) -> int:
        try:
            return self.db.rpush(self.name, value)
        except Exception as e:
            return e

    def read(self ) -> [bytes]:
        try:
            return self.db.lpop(self.name)
        except Exception as e:
            return e

class Stack:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, value: str) -> int:
        try:
            return self.db.lpush(self.name, value)
        except Exception as e:
            return e

    def read(self ) -> [bytes]:
        try:
            return self.db.lpop(self.name)
        except Exception as e:
            return e

class Delete:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def delete(self) -> bool:
        try:
            return self.db.delete(self.name) == 1
        except Exception as e:
            return e



