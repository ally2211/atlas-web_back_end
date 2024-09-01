#!/usr/bin/env python3
'''
  Async Comprehensions
'''
import asyncio
import random
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    returns sum of lists
    '''
    start_time = time.perf_counter()  # Record start time
    # Run four instances of async_comprehension in parallel
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    end_time = time.perf_counter()  # Record end time

    # Calculate total runtime
    total_sum = end_time - start_time
    return total_sum
