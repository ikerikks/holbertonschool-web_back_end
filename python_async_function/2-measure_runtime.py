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
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time = float(total_time / n)
    return average_time

if __name__ == "__main__":
    n = 5
    max_delay = 9
    asyncio.run(measure_time(n, max_delay))
    
