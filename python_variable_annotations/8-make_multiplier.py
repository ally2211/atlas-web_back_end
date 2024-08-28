#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(y: float) -> Callable[[float], float]:
    """
    create multiplier
    """
    def multiplier(k: float) -> float:
        """
        multiplier
        """
        return (k * y)
    return multiplier
