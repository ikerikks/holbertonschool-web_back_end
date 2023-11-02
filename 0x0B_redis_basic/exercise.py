#!/usr/bin/env python3
""" redis basic"""
import redis
import uuid
from typing import Union, Callable
import functools


class Cache:
    """ Cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data"""
        key = str(uuid.uuid4())
        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(key, data)
            return key
        else:
            raise ValueError("Data must be a string, bytes, int, or float.")

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int]:
        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> Union[str, bytes, int]:
        return self.get(key, fn=lambda data: data.decode("utf-8"))

    def get_int(self, key: str) -> Union[str, bytes, int]:
        return self.get(key, fn=int)

    def count_calls(method: Callable) -> Callable:
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            count = self._redis.incr(key)
            result = method(self, *args, **kwargs)
            return result

        return wrapper


Cache.store = Cache.count_calls(Cache.store)
