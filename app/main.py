from redis_package.redis_operation import RedisClient
from redis_package.config import redis_config

# Initialize Redis client
client = RedisClient(config=redis_config)

class Queue:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, item):
        try:
            self.client.pushr(self.name, item)
            return
        except Exception as e:
            return e

    def read(self):
        try:
            return self.client.popl(self.name)
        except Exception as e:
            return e

class Stack:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, item):
        try:
            self.client.pushl(self.name, item)
            return
        except Exception as e:
            return e

    def read(self):
        try:
            return self.client.popl(self.name)
        except Exception as e:
            return e

class Delete:
    def __init__(self, client):
        self.client = client

    def delete(self, name):
        try:
            if self.client.delete(name):
                return True
            else:
                return False
        except Exception as e:
            return e


