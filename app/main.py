from redis_package.redis_operation import RedisClient
from redis_package.config import redis_config

# Initialize Redis client
client = RedisClient(config=redis_config)


def push_items(pairs: str):
    try:
        pairs_list = pairs.split('/')
        if len(pairs_list) % 2 != 0:
            raise ValueError("Invalid number of parameters. Must be in key/value pairs.")

        count = 0
        for i in range(0, len(pairs_list), 2):
            key = pairs_list[i]
            value = pairs_list[i + 1]
            client.push(key, value)
            count += 1

        return f"Pushed {count} items. Current queue lengths: {get_all_lengths()}"
    except Exception as e:
        return str(e)


def pop_item(key: str):
    try:
        item = client.pop(key)
        return f"Popped item: {item.decode('utf-8') if item else 'Queue is empty'}"
    except Exception as e:
        return str(e)


def get_all_items():
    try:
        keys = client.get_all_keys()
        all_items = {key.decode('utf-8'): [item.decode('utf-8') for item in client.get_all(key.decode('utf-8'))] for key
                     in keys if client.is_list(key.decode('utf-8'))}
        return all_items
    except Exception as e:
        return str(e)


def remove_item(key: str, value: str):
    try:
        count = client.remove(key, value)
        return f"Removed {count} instances of {value} from {key}"
    except Exception as e:
        return str(e)


def update_item(key: str, index: int, value: str):
    try:
        success = client.update(key, index, value)
        if success:
            return f"Updated item at index {index} in {key} to {value}"
        else:
            return f"Failed to update item at index {index} in {key}"
    except Exception as e:
        return str(e)


def get_all_lengths():
    try:
        keys = client.get_all_keys()
        lengths = {key.decode('utf-8'): client.len(key.decode('utf-8')) for key in keys if
                   client.is_list(key.decode('utf-8'))}
        return lengths
    except Exception as e:
        return str(e)


# Example usage (optional):
if __name__ == "__main__":
    pairs = "key1/value1/key2/value2"
    print(push_items(pairs))

    key = "key1"
    print(pop_item(key))

    print(get_all_items())

    key = "key1"
    value = "value1"
    print(remove_item(key, value))

    key = "key1"
    index = 0
    value = "new_value"
    print(update_item(key, index, value))
