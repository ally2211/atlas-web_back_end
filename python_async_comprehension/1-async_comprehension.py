#!/usr/bin/env python3
'''
  Async Comprehensions
'''
import asyncio
import random
from typing import AsyncGenerator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_comprehension() -> float:
    '''
    loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)  # Yield a random integer between 0 and 10
