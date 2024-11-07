from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    api_port: int = 80
    api_forward_port: int = 8080
    db_host: str
    db_name: str
    db_user: str
    db_password: str
    db_port: int = 5432
    db_forward_port: int = 5433
    db_driver: str = "postgresql+psycopg2"

    @property
    def db_url(self):
        return f"{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

@lru_cache
def get_settings():
    return Settings()

engine = create_engine(get_settings().db_url)

def get_session():
    with Session(engine) as session:
        yield session
