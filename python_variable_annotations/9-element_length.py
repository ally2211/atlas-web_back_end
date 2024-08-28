#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    return length of list
    '''
    return [(i, len(i)) for i in lst]
