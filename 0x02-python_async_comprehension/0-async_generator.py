#!/usr/bin/env python3
'''Coroutine that generates random numbers asynchronously.'''
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    '''Generate random numbers asynchronously.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10