#!/usr/bin/env python3
"""
Task #1: multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    multiple coroutines at the same time with async
    :param n:
    :param max_delay:
    :return:
    """
    nums = list()
    for i in range(n):
        nums.append(await wait_random(max_delay))
    return sorted(nums)
