import os
from pydantic import BaseSettings
from dotenv import dotenv_values


class GlobalSettings(BaseSettings):
    class Config:
        env_file: str = ".env"
        BASEDIR: str = os.path.abspath(os.path.dirname(__file__))


dotenv_values = dotenv_values(GlobalSettings.Config.env_file)


def get_config():
    return dotenv_values
