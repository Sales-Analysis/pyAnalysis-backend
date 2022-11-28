from pydantic import BaseSettings
from dotenv import load_dotenv


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

load_dotenv()


class GlobalSettings(BaseSettings):
    IP: str = "127.0.0.1"
    PORT: int = 9090

    class Config:
        env_file: str = ".env"


def get_config():
    return GlobalSettings()
