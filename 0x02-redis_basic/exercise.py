#!/usr/bin/env python3
"""
redis
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache:
    """
    cashe class
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        return key after storing input
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """
        call data
        """
        value = self._redis.get(key)
        if fn and value is not None:
            return fn(value)

        return value

    def get_str(self, key: str) -> str:
        """
        get a string
        """
        value = self._redis.get(key)
        return value.decode('utf-8') if value else ""

    def get_int(self, key: str) -> int:
        """
        get an int
        """
        value = self._redis.get(key)
        return int(value.decode('utf-8')) if value else 0
