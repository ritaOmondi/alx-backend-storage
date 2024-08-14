#!/usr/bin/env python3
"""
This module contains the Cache class, which provides a simple interface
for storing and retrieving data using Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional

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

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """
        Retrieves the data stored at the given key in Redis.

        Args:
            key (str): The key for the stored data.
            fn (Optional[Callable[[bytes], Any]]): A function to convert the retrieved
                data to the desired format. If not provided, the raw bytes will be returned.

        Returns:
            Any: The data stored at the given key, converted using the provided function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        else:
            return fn(data)

    def get_str(self, key: str) -> str:
        """
        Retrieves the data stored at the given key in Redis as a string.

        Args:
            key (str): The key for the stored data.

        Returns:
            str: The data stored at the given key, converted to a string.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieves the data stored at the given key in Redis as an integer.

        Args:
            key (str): The key for the stored data.

        Returns:
            int: The data stored at the given key, converted to an integer.
        """
        return self.get(key, int)
