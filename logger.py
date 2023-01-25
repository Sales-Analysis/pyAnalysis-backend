import logging
from logging.config import dictConfig


LOGGING_CONF = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s: |%(name)s| %(message)s'
        }
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        '': {
            'handlers': ['stdout'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}


dictConfig(LOGGING_CONF)
logger = logging.getLogger(__name__)

