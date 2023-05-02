#!/usr/bin/env python3
"""
4. Tasks
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    multiple coroutine'd-tasks at the same time with async
    :param n:
    :param max_delay:
    :return:
    """
    nums = list()
    for i in range(n):
        nums.append(await task_wait_random(max_delay))
    return sorted(nums)
