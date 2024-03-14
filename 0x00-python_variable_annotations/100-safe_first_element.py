#!/usr/bin/env python3
"""Task 100 module that takes a sequence lst and returns its first element."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """function that takes a sequence lst and returns its first element."""
    return lst[0] if lst else None