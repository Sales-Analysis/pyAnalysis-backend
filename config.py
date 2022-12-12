import os
import shutil
from pydantic import BaseSettings
from dotenv import dotenv_values


LOG_FORMAT = "%(levelprefix)s %(asctime)s - %(message)s"
LOGGER_CONF = {
    "dev": {
        "version": 1,
        "loggers": {
            "fastapi": {"level": "DEBUG", "handlers": ["console_handler"]},
            "uvicorn": {
                "handlers": ["console_handler"],
            },
        },
        "formatters": {
            "console": {
                "()": "uvicorn.logging.DefaultFormatter",
                "format": LOG_FORMAT,
            }
        },
        "handlers": {
            "console_handler": {
                "formatter": "console",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
    }
}


class GlobalSettings(BaseSettings):
    class Config:
        env_file: str = ".env"
        BASEDIR: str = os.path.abspath(os.path.dirname(__file__))


dotenv_values = dotenv_values(GlobalSettings.Config.env_file)


def get_config():
    return dotenv_values


def create_temp_dir():
    temp_dir = f'{GlobalSettings.Config.BASEDIR}/data/temp'
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)


def del_temp_dir():
    temp_dir = f'{GlobalSettings.Config.BASEDIR}/data/temp'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
