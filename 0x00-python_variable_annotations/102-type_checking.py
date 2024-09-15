#!/usr/bin/env python3
"""
Checking type
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """multiple copies of items in a tuple"""
    zoomed_in_list: List = [
        i for i in lst
        for j in range(factor)
    ]
    return zoomed_in_list


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
