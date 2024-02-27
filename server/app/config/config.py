
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):

    model_config= SettingsConfigDict(env_file=".env")
    DB_URL ="postgres://zyhaxiam:EHNQbkPk_-lPNqo8dLb3hV40blIvU9sN@stampy.db.elephantsql.com/zyhaxiam"
    DB_PASSWORD ="EHNQbkPk_-lPNqo8dLb3hV40blIvU9sN"
    DB_NAME="zyhaxiam"