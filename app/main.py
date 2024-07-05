from redis_package.redis_operation import RedisClient, Queue
from redis_package.config import redis_config

# Initialize Redis client
client = RedisClient(config=redis_config)

class Queue:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, item):
        try:
            self.client.push(self.name, item)
            return True
        except Exception as e:
            print(f"Error writing to queue '{self.name}': {str(e)}")
            return False

    def read(self):
        try:
            return self.client.pop(self.name)
        except Exception as e:
            print(f"Error reading from queue '{self.name}': {str(e)}")
            return None
