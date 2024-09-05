#!/usr/bin/env python3
"""
This module contains an async function that spawns n instances of wait_random.
"""


from typing import List
import asyncio
import heapq
wait_random= __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    # Spawn all wait_random coroutines
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # Use asyncio.gather to collect the results
    delays = await asyncio.gather(*tasks)
    
    # Return the delays sorted in ascending order (using heapq.nsmallest)
    return list(heapq.nsmallest(n, delays))  # Efficient sorting without sort()
