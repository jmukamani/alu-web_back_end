#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier function.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, where each tuple contains a sequence from the input iterable
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., strings or lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence from the
                                     input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
