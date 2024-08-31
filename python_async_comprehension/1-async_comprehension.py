#!/usr/bin/env python3
'''
  Async Comprehensions
'''
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    returns list of floats
    '''
    return [x async for x in async_generator()]
