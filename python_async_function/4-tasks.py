#!/usr/bin/env python3
'''
tasks
'''
import asyncio
from typing import List


# wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    displays a list of random numbers
    '''
    result = []
    for num in range(n):
        randomNumber = await task_wait_random(max_delay)
        result.append(randomNumber)

    return sorted(result)

if __name__ == "__main__":
    n = 5
    max_delay = 6
    result = asyncio.run(task_wait_n(n, max_delay))
    print(result)
