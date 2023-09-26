import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension() four times in parallel.
    """
    start_time = time.time()

    for i in range(4):
        await asyncio.gather(async_comprehension())

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime 
