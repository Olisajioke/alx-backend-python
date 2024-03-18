#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine to spawn wait_random n times."""
    return sorted(await asyncio.gather(*(wait_random(max_delay)
                                         for _ in range(n))))