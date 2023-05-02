#!/usr/bin/env python3
"""
Task 0. The basics of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random value between 0 and `max_delay`
    :param max_delay:
    :return:
    """
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
