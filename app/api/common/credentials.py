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

    @classmethod
    def get_database_url(cls):
        # return f'postgresql+psycopg2://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}' \
            # f'@{cls.POSTGRES_SERVER}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}'
        return 'postgresql+psycopg2://tnqrjszpbdwfzo:59deba175f8192f1c274efda57a62ec4f9f7d656078bf69d1c8bc4d640267414@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d6map5821v2dop'


class CredentialsJWT:
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
    JWT_EXPIRES_MINUTES: int = int(os.getenv('JWT_EXPIRES_MINUTES'))
    JWT_TOKEN_URL: str = os.getenv('JWT_TOKEN_URL')

