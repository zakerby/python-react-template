import os


class Parse:
    """Class of utility functions to parse environment variables"""

    @staticmethod
    def bool(field):
        """Parse booleans (defaults to False)"""
        return os.getenv(field, '').lower() in ['true', '1']


class Settings:

    # General
    DEV = Parse.bool('DEV')
    REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
    REDIS_URL = f'redis://{REDIS_HOST}:6379'

    # Database
    AES_SECRET_KEY = os.getenv('AES_SECRET_KEY', 'fake-aes-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    # Celery
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_CONFIG = {
        'beat_schedule': {
            'ping_once': {
                'task': 'lwca.tasks.ping_once',
                'args': (1,),
                'schedule': 60.0,
            },
        }
    }

    # Ollama
    OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'ollama')
    OLLAMA_PORT = os.getenv('OLLAMA_PORT', '11434')
    OLLAMA_URL = f'http://{OLLAMA_HOST}:{OLLAMA_PORT}'
    OLLAMA_DEFAULT_MODEL = os.getenv('OLLAMA_DEFAULT_MODEL', 'deepseek-coder:1.3b-instruct')

    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fake-jwt-key')
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600)

    # ChromaDB
    CHROMADB_HOST = os.getenv('CHROMADB_HOST', 'chromadb')
    CHROMADB_PORT = os.getenv('CHROMADB_PORT', '8081')