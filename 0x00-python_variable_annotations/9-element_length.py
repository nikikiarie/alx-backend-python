#!/usr/bin/env python3
'''iterable object
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''list of tuples with the length of each element
    '''
    return [(j, len(j)) for j in lst]
