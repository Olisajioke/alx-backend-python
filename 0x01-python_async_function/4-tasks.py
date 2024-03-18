#!/usr/bin/env python3
'''Task 4's module.'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Measures the total execution time for `n` calls to task_wait_random.'''
    return await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
