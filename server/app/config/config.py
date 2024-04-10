
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):

    DB_URL:str =''
    DB_PASSWORD:str=''
    DB_NAME:str=''
    PORT:int=0
    
    HOST:str=''
    model_config= SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')
    