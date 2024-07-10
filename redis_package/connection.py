# redis_package/connection.py

import redis
from .config import redis_config

def connect(config=None):
    config = redis_config
    return redis.Redis(**config)
