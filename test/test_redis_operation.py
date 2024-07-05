import pytest
from redis_package.redis_operation import RedisClient
from redis_package.config import redis_config

# Initialize Redis client for testing
@pytest.fixture(scope="module")
def redis_client():
    return RedisClient(config=redis_config)

def test_push(redis_client):
    pairs = input("Enter key-value pairs separated by '/': ")
    try:
        pairs_list = pairs.split('/')
        if len(pairs_list) % 2 != 0:
            raise ValueError("Invalid number of parameters. Must be in key/value pairs.")

        count = 0
        for i in range(0, len(pairs_list), 2):
            key = pairs_list[i]
            value = pairs_list[i + 1]
            result = redis_client.push(key, value)
            assert result >= 1  # Assuming each push returns >= 1 for success
            count += 1

        print(f"{count} items pushed successfully.")
    except Exception as e:
        print(str(e))


def test_pop(redis_client):
    key = input("Enter the key to pop from: ")
    result = redis_client.pop(key)
    if result:
        print(f"Popped item: {result.decode('utf-8')}")
    else:
        print("Queue is empty")

def test_get_all(redis_client):
    key = input("Enter the key to get all items from: ")
    result = redis_client.get_all(key)
    if result:
        items = [item.decode('utf-8') for item in result]
        print(f"All items in {key}: {items}")
    else:
        print("Queue is empty")

def test_remove(redis_client):
    key = input("Enter the key to remove from: ")
    value = input("Enter the value to remove: ")
    result = redis_client.remove(key, value)
    print(f"Removed {result} instances of {value} from {key}")

def test_update(redis_client):
    key = input("Enter the key to update: ")
    index = int(input("Enter the index to update: "))
    value = input("Enter the new value: ")
    success = redis_client.update(key, index, value)
    if success:
        print(f"Updated item at index {index} in {key} to {value}")
    else:
        print(f"Failed to update item at index {index} in {key}")

def test_len(redis_client):
    key = input("Enter the key to get length: ")
    result = redis_client.len(key)
    print(f"Length of {key}: {result}")

def test_is_list(redis_client):
    key = input("Enter the key to check if it's a list: ")
    if redis_client.is_list(key):
        print(f"{key} is a list")
    else:
        print(f"{key} is not a list")


if __name__ == "__main__":
    pytest.main()
