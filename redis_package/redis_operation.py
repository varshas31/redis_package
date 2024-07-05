import redis
from .config import redis_config

class Queue:
    def __init__(self, client: redis.Redis, name: str):
        self.client = client
        self.name = name

    def read(self):
        """
        Reads and removes the last item from the queue.

        Returns:
            str: Item read from the queue.
        """
        return self.client.lpop(self.name)

    def write(self, value: str):
        """
        Writes an item to the end of the queue.

        Args:
            value (str): Value to be pushed to the queue.
        """
        self.client.rpush(self.name, value)
