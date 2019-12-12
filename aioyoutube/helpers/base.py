from functools import wraps
from rfc3339 import rfc3339
from datetime import datetime


def insert_name(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator insert class method name into this method parameters."""
        return await coroutine(*args, **kwargs, name=coroutine.__name__)

    return wrapper


def time_converting(time: int):
    """Converting time format from unixtime to rfc3339."""
    return rfc3339(datetime.fromtimestamp(time), utc=True)
