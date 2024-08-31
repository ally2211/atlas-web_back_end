#!/usr/bin/env python3
'''
The basics of async
'''
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List, Iterable


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    return a list that calls wait_random and returns random delays that are sorted
    '''
    tasks=[]
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    
     # Implementing selection sort to sort the list
    for i in range(len(delays)):
        min_index = i
        for j in range(i + 1, len(delays)):
            if delays[j] < delays[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        delays[i], delays[min_index] = delays[min_index], delays[i]
    return delays
