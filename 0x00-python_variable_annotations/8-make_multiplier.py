#!/usr/bin/env python3
"""Module that takes a float as argument and returns a function that multiplies a float by a given multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its input by a given multiplier."""
    return lambda x: x * multiplier
