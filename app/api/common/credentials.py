import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)


class CredentialsDB:
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    HEROKU_URL = 'jtlvyhctfevcwz:d51f070f3eeb305dce27536c45395896e6ed9a0d85e229c41005745824af841a@ec2-99-81-137-11.eu-west-1.compute.amazonaws.com:5432/d6d6d1leanpbnn'

    @classmethod
    def get_database_url(cls):
        return f'postgresql+psycopg2://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}' \
            f'@{cls.POSTGRES_SERVER}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}'
        # return f'postgresql+psycopg2://{cls.HEROKU_URL}'


class CredentialsJWT:
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
    JWT_EXPIRES_MINUTES: int = int(os.getenv('JWT_EXPIRES_MINUTES'))
    JWT_TOKEN_URL: str = os.getenv('JWT_TOKEN_URL')

