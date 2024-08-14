#!/usr/bin/env python3
"""
This module contains the Cache class, which provides a simple interface
for storing and retrieving data using Redis.
"""

import redis
import uuid
from typing import Union

class Cache:
    """
    A simple cache implementation using Redis.

    Attributes:
        _redis (redis.Redis): A private instance of the Redis client.
    """

    def __init__(self) -> None:
        """
        Initializes the Cache instance and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the provided data in Redis and returns the generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The generated key for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
