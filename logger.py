from logging.config import dictConfig
from fastapi.logger import logger
from config import get_config

logger = logger
settings = get_config()

dictConfig(settings.LOGGER_CONF["dev"])
