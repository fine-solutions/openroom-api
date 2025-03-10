from os import path
from pydantic_settings import BaseSettings, SettingsConfigDict



class Config(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=path.abspath(__file__).replace('config.py', '.env'))

    def get_db_url(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    


conf = Config()
