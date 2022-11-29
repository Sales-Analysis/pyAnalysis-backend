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


dotenv_values = dotenv_values(GlobalSettings.Config.env_file)


def get_config():
    return dotenv_values
