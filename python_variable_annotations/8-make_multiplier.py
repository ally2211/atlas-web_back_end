#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(m: float) -> Callable[[float], float]:
    """
    create multiplier
    """
    def multiplier(k: float) -> float:
        """
        multiplier
        """
        return (k * m)
    return multiplier
