#!/usr/bin/env python3
'''
 Async Generator
'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)  # Yield a random integer between 0 and 10
