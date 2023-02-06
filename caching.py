from functools import lru_cache, wraps
from datetime import datetime, timedelta


def lry_cache(seconds: int, maxsize: int = 128):
    def cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime
                return func(*args, **kwargs)

        return wrapped_func

    return cache
