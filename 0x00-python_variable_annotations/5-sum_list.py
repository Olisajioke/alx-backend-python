#!/usr/bin/env python3
"""Module that takes a list of floats as argument and returns their sum."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all elements in a list of floats."""
    return float(sum(input_list))
