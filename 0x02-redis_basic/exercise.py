#!/usr/bin/env python3
"""
redis
"""
import redis
from uuid import uuid4


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

    def store(self, data: any) -> str:
        """
        return key after storing input
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
