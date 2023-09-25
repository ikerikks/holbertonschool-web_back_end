#!/usr/bin/env python3

import asyncio
import random as rand


async def wait_random(max_delay=10):
    """Wait for a random number of seconds"""
    randNumber = rand.uniform(0, max_delay)
    await asyncio.sleep(randNumber)
    return randNumber
