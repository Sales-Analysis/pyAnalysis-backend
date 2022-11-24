from logging.config import dictConfig
from fastapi.logger import logger
from config import LOGGER_CONF

logger = logger
dictConfig(LOGGER_CONF["dev"])
