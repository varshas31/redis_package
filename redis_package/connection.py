# redis_package/connection.py

import redis
from .config import redis_config

def connect(config=None):
    """
    Initialize a Redis connection with the given configuration.

    Args:
        config (dict, optional): Dictionary containing Redis connection parameters. Defaults to None.

    Returns:
        redis.Redis: Redis client instance.
    """
    config = redis_config
    return redis.Redis(**config)
