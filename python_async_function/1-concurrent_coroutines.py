#!/usr/bin/env python3
'''
cocurrent coroutines
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    displays a list of random numbers
    '''
    result = []
    for num in range(n):
        randomNumber = await wait_random(max_delay)
        result.append(randomNumber)

    return sorted(result)
