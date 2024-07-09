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

if __name__ == "__main__":
    pytest.main()
