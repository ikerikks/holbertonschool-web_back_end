#!/usr/bin/env python3
'''
parallel runtime
'''
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(),  async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
