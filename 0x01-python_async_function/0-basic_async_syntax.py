#!/usr/bin/env python3
'''Module for the wait_random function.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''function that takes in an integer argument'''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
