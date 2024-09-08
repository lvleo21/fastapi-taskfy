from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
        env_file_encoding='utf-8'
    )

    TASKFY_VERSION: str = "v1.0.0"

    PROJECT_NAME: str = "Taskfy"
    DATABASE_URL: str = ""

    REDIS_HOST: str = "127.0.0.1"
    REDIS_PORT: int = 6379

    PAGINATION_LIMIT: int = 100
    PAGINATION_OFFSET: int = 0


settings = Settings()
