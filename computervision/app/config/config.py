
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):

    model_config= SettingsConfigDict(env_file=".env")
    DB_URL:str
    DB_PASSWORD:str
    DB_NAME:str
    PORT:int
    
    HOST:str