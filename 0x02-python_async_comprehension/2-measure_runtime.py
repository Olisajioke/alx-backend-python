#!/usr/bin/env python3
'''
Coroutine to measure the total runtime of executing
async_com multiple times in parallel.
'''
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measure the total runtime of executing async_com 4x in parallel.'''
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time


async def main():
    '''Run measure_runtime and return the result.'''
    return await measure_runtime()


if __name__ == "__main__":
    print(asyncio.run(main()))
