from os import path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field



class Config(BaseSettings):
    DB_USER: str = Field(alias='POSTGRES_USER')
    DB_PASSWORD: str = Field(alias='POSTGRES_PASSWORD')
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str = Field(alias='POSTGRES_DB')

    JWT_SECRET_KEY: str
    JWT_ACCESS_TTL: int
    JWT_REFRESH_TTL: int

    API_PORT: int

    model_config = SettingsConfigDict(env_file=path.abspath(__file__).replace('config.py', '.env'))

    def get_db_url(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    


conf = Config()
