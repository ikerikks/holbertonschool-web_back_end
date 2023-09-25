#!/usr/bin/env python3
'''
measure runtime
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''
    Measure the total execution time
    '''
    start_time = time.time()
    await wait_n(n, max_delay)  # Call the wait_n function from the other module
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
