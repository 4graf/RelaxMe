from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

load_dotenv()


class EndpointSettings(BaseSettings):
    stress_service_endpoint: str


class DatabaseSettings(BaseSettings):
    """
    Настройки к базе данных.

    Attributes:
        postgres_url: Строка подключения к PostgreSQL.
        # redis_url: Строка подключения к Redis.
    """
    postgres_url: PostgresDsn
    # redis_url: RedisDsn
