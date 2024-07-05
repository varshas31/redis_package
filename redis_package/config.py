from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

redis_config = {
    'host': os.getenv('REDIS_HOST', 'localhost'),
    'port': int(os.getenv('REDIS_PORT', 6379)),
    'db': int(os.getenv('REDIS_DB', 0))
}
