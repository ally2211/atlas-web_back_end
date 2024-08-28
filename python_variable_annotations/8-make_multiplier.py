#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    create multiplier
    """
    def multiply(k: float) -> float:
        """
        multiplier
        """
        return (k * multiplier)
    return multiply
