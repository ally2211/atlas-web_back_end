#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        init
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Skip the header (first row) and cache the data
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get page
        """
        # Assert that the page number is positive
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        # Ensure the dataset is loaded
        self.__dataset = self.dataset()

        start_index, end_index = self.index_range(page, page_size)
        return self.__dataset[start_index:end_index]

    def index_range(self, page, page_size):
        """
        create pagination tuple
        """
        start_index = (page - 1) * page_size
        end_index = page * page_size
        tupleindex = (start_index, end_index)
        return tupleindex
