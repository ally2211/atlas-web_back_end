#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    create pagination tuple
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    tupleindex = (start_index, end_index)
    return tupleindex
