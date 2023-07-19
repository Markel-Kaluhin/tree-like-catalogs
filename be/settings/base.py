import os
from functools import lru_cache
from os.path import abspath, dirname

from pydantic import BaseSettings

BASE_DIR = dirname(dirname(abspath(__file__)))


class Settings(BaseSettings):
    sqlalchemy_host: str
    sqlalchemy_port: int
    sqlalchemy_db_name: str
    sqlalchemy_user: str
    sqlalchemy_password: str
    app_host: str
    app_port: int
    reload_app: bool
    allow_origins: str
    application_name: str

    class Config:
        env_file = os.path.join(BASE_DIR, ".env")


@lru_cache()
def get_settings() -> Settings:
    _settings = Settings()
    return _settings


settings = get_settings()


@lru_cache()
def build_sqlalchemy_database_uri() -> str:
    db_url = (
        f"postgresql+asyncpg://{settings.sqlalchemy_user}:{settings.sqlalchemy_password}"
        f"@{settings.sqlalchemy_host}:{settings.sqlalchemy_port}/{settings.sqlalchemy_db_name}"
    )
    return db_url
