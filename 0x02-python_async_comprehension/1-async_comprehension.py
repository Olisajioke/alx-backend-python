#!/usr/bin/env python3
'''Coroutine to collect 10 random numbers async using async comprehensions.'''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collect 10 random numbers using async comprehension.'''
    return [rand_num async for rand_num in async_generator()]


async def main():
    '''Run async_comprehension and print the result.'''
    print(await async_comprehension())


if __name__ == "__main__":
    asyncio.run(main())
