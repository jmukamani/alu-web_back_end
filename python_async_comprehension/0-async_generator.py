#!/usr/bin/env python3
"""
This module contains a coroutine
that yields random numbers asynchronously.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields a random number between 0 and 10.

    The coroutine loops 10 times,
    each time asynchronously waiting for 1 second.
    
    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait asynchronously for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
