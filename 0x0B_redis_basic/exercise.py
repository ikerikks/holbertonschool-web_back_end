#!/usr/bin/env python3
""" redis basic"""
import redis
import uuid


class Cache:
    """ Cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str) -> str:
        """ Store data"""
        key = str(uuid.uuid4())
        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(key, data)
            return key
        else:
            raise ValueError("Data must be a string, bytes, int, or float.")
