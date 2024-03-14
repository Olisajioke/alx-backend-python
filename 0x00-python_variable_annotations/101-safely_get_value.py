#!/usr/bin/env python3
"""module that takes a float n as argument and returns the floor of the float."""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """function that takes a float n as argument and returns the floor of the float."""
    if key in dct:
        return dct[key]
    else:
        return default
