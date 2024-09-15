#!/usr/bin/env python3
"""first element of a sequence
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the 1st list element or None if empty."""
    if lst:
        return lst[0]
    else:
        return None
