#!/usr/bin/env python3
"""module sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list containing both integers and floats."""
    return float(sum(mxd_lst))