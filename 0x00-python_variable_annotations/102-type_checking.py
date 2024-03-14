#!/usr/bin/env python3
"""Module that takes a sequence lst and returns its first element."""
from typing import List, Tuple, Union, Sequence


def zoom_array(
    lst: Union[Sequence[int], Tuple[int, ...]], factor: int = 2
) -> List[int]:
    """function that takes a sequence lst and returns its first element."""
    zoomed_in: List[int] = [
        item
        for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
