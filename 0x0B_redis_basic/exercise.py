#!/usr/bin/env python3
""" redis basic"""
import redis
import uuid
from typing import Union, Callable
import functools


def count_calls(method: Callable) -> Callable:
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

    @count_calls
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


def call_history(method: Callable) -> Callable:
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
    cache = Cache()

    keys = cache._redis.keys(f"{func.__qualname__}:*")

    if not keys:
        print(f"{func.__qualname__} was not called.")
        return

    inputs = []
    outputs = []

    for key in keys:
        inputs_key = f"{key}:inputs"
        outputs_key = f"{key}:outputs"

        inputs.extend(cache._redis.lrange(inputs_key, 0, -1))
        outputs.extend(cache._redis.lrange(outputs_key, 0, -1))

    inputs = [eval(input_data.decode('utf-8')) for input_data in inputs]
    outputs = [output.decode('utf-8') for output in outputs]

    print(f"{func.__qualname__} was called {len(keys)} times:")

    for i, (input_data, output) in enumerate(zip(inputs, outputs), 1):
        print(f"{func.__qualname__}(*{input_data}) -> {output}")


Cache.store = count_calls(Cache.store)
Cache.store = call_history(Cache.store)
