#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List
import math


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
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

        # get the data for the current page
        data = self.get_page(page, page_size)

        # calculate total number of items in the dataset
        total_items = len(self.__dataset)

        # calculate total pages
        total_pages = math.ceil(total_items / page_size)

        # determine next page
        next_page = page + 1 if page < total_pages else None

        # determine prev_page (none if first page)
        prev_page = page - 1 if page > 1 else None

        start_index, end_index = self.index_range(page, page_size)
        return {'page_size': len(data),
                'page': page,
                'data': self.__dataset[start_index:end_index],
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages}

    def index_range(self, page, page_size):
        """
        create pagination tuple
        """
        start_index = (page - 1) * page_size
        end_index = page * page_size
        tupleindex = (start_index, end_index)

        return tupleindex
