from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

redis_config = {
    'host': os.getenv('REDIS_HOST'),
    'port': int(os.getenv('REDIS_PORT')),
    'db': int(os.getenv('REDIS_DB'))
}
