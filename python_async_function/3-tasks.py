#!/usr/bin/env python3
'''
tasks
'''
import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task[Awaitable[float]]:
    return asyncio.Task(wait_random(max_delay))
