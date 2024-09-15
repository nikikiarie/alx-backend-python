#!/usr/bin/env python3
'''Tasks
'''
import asyncio
from typing import List


task_wait = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''runs task_wait_random n times.
    '''
    delay_time = await asyncio.gather(
        *tuple(map(lambda _: task_wait(max_delay), range(n)))
    )
    return sorted(delay_time)
