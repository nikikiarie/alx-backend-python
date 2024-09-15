#!/usr/bin/env python3
'''multiplies a float by multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplier function.
    '''
    return lambda x: x * multiplier
