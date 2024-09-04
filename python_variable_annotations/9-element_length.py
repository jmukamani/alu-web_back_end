#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier function.
"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Return a list of tuples, where each tuple contains a string from the input list
    and its corresponding length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, each containing a string from the
                               input list and its length.
    """
    return [(i, len(i)) for i in lst]
