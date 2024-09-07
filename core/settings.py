from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    PROJECT_NAME: str = "Taskfy"
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    DB_HOST: str
    DB_PORT: int = 5432
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str = ""

    REDIS_HOST: str = "127.0.0.1"
    REDIS_PORT: int = 6379

    PAGINATION_LIMIT: int = 100
    PAGINATION_OFFSET: int = 0
    SQLALCHEMY_DATABASE_URI: str = ""


settings = Settings()
