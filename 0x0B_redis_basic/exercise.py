#!/usr/bin/env python3
""" redis basic"""
import redis
import uuid
from typing import Union, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """ count calls"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        count = self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


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
        """ Get data from cache"""
        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> Union[str, bytes, int]:
        """ Get str data """
        return self.get(key, fn=lambda data: data.decode("utf-8"))

    def get_int(self, key: str) -> Union[str, bytes, int]:
        """ Get int data """
        return self.get(key, fn=int)


def call_history(method: Callable) -> Callable:
    """ Call"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        input_args = str(args)
        self._redis.rpush(inputs_key, input_args)
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)
        return output
    return wrapper


def replay(func: Callable) -> None:
    """ Replay"""
    cache = Cache()
    key_pattern = f"{func.__qualname__}:*"
    keys = cache._redis.keys(key_pattern)

    if not keys:
        print(f"{func.__qualname__} was not called.")
        return

    calls = []

    for key in keys:
        inputs_key = f"{key}:inputs"
        outputs_key = f"{key}:outputs"

        inputs = cache._redis.lrange(inputs_key, 0, -1)
        outputs = cache._redis.lrange(outputs_key, 0, -1)

        for input_data, output in zip(inputs, outputs):
            calls.append((input_data, output))

    print(f"{func.__qualname__} was called {len(calls)} times:")

    for i, (input_data, output) in enumerate(calls, 1):
        input_str = input_data.decode("utf-8")
        print(f"{func.__qualname__}(*{input_str}) -> {output.decode('utf-8')}")


Cache.store = count_calls(Cache.store)
Cache.store = call_history(Cache.store)
