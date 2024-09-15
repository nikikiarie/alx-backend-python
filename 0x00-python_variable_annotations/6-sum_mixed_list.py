#!/usr/bin/env python3
'''Mixed list
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Sum of a list of int and float.
    '''
    return float(sum(mxd_lst))
