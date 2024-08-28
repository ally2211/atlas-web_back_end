#!/usr/bin/env python3
"""
 Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(numbers: List[Union[int, float]]) -> float:
    """
    Sum a list of mixed types
    """
    return round(sum(numbers), 2)
