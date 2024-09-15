#!/usr/bin/env python3
"""More involved type annotations
"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Gets value from dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return
