#!/usr/bin/env python3
'''Coroutine that generates random numbers asynchronously.'''
import asyncio
import random


async def async_generator():
    '''Generate random numbers asynchronously.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    '''Prints values yielded by async_generator.'''
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)


if __name__ == "__main__":
    asyncio.run(print_yielded_values())
