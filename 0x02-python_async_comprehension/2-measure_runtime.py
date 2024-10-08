#!/usr/bin/env python3
'''Run time for four parallel comprehensions
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''runs async_comprehension 4 times
    '''
    initTime = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - initTime
