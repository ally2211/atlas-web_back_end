#!/usr/bin/env python3
'''
Measure the runtime
'''
import asyncio
import random
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measures the total execution time 
    '''
     # Run the asynchronous code in an event loop and get the result
    return asyncio.run(_measure_time_async(n, max_delay))

async def _measure_time_async(n: int, max_delay: int) -> float:
    delays = await wait_n(n, max_delay)
    total_time = sum(delays)
    return total_time / n
