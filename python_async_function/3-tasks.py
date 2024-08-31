#!/usr/bin/env python3
'''
Return a task using a def
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    return an asyncio task
    '''
    task = asyncio.create_task(wait_random(max_delay))
    return task
