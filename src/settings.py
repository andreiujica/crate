from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_NAME: str = "Crate"
    API_VERSION: str = "0.1.0"
    API_DESCRIPTION: str = "Webhook-based FastAPI service for file classification in data workflows."
    LOGGING_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()