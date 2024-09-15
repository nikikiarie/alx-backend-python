#!/usr/bin/env python3
'''Async Comprehensions
'''
from typing import List
from importlib import import_module as using


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''generates a list of 10 numbers from a 10-number generator.
    '''
    return [i async for i in async_generator()]
