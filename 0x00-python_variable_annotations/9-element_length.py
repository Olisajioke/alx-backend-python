#!/usr/bin/env python3
"""module that takes an iterable and returns a list of tuples with the length of each element"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that takes an iterable and returns a list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]
