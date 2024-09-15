#!/usr/bin/env python3
'''Basics of async
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits a num of random seconds
    '''
    random_time = random.random() * max_delay
    await asyncio.sleep(random_time)
    return random_time
