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

