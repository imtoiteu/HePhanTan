import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    GATEWAY_TIMEOUT: int = 59


settings = Settings()