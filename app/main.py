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

# Example usage:
if __name__ == "__main__":
    queue_name = "my_queue"
    queue = Queue(client, queue_name)

    # Write to queue
    item_to_write = "Hello, Redis!"
    queue.write(item_to_write)

    # Read from queue
    item_read = queue.read()
    print(f"Read from queue '{queue_name}': {item_read.decode('utf-8') if item_read else None}")
