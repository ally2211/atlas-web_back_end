#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    create multiplier
    """
    def multiplier(k: float) -> float:
        """
        multiplier
        """
        return (k * k)
    return multiplier
