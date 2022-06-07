import os
from dotenv import load_dotenv


env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)


class CredentialsJWT:
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
    JWT_EXPIRES_MINUTES: int = int(os.getenv('JWT_EXPIRES_MINUTES'))
    JWT_TOKEN_URL: str = os.getenv('JWT_TOKEN_URL')
