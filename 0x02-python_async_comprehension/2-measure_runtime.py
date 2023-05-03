#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.

    measure_runtime should measure the total runtime and return it.

    Notice that the total runtime is roughly 10 seconds, explain it to
    yourself.
    Explanation: [`async_generator` (the main async task being invoked (from
    task#0)) runs 10 times with asyncio.sleep every second, so every
    co-routine `gathered` will not exceed that 10 seconds window by much]
    :return: the total execution time measured for all the co-routines
    """
    start = time.time()
    tasks_generator = (async_comprehension() for i in range(4))
    await asyncio.gather(*tasks_generator)
    return time.time() - start
