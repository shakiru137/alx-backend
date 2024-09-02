#!/usr/bin/env python3
"""Task 3: Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None  # Initialize indexed dataset

    def dataset(self) -> List[List]:
        """Cached dataset.

        Returns:
            List[List]: The dataset, where each entry is a list of data fields.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List]: The dataset indexed by its original position.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.

        Args:
            page (int): The current page number (must be > 0).
            page_size (int): The number of items per page (must be > 0).

        Returns:
            List[List]: A list of lists containing the data for the requested
            page.

        Raises:
            AssertionError: If 'page' or 'page_size' is not a positive integer.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Retrieves info about a page from a given index with a specified
        size.

        Args:
            index (int): The index to start retrieving data from.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing information about the page.

        Raises:
            AssertionError: If 'index' is out of range.
        """
        data = self.indexed_dataset()
        assert index >= 0 and index <= max(data.keys())

        page_data = []
        data_count = 0
        next_index = None
        start = index if index else 0

        for i, item in data.items():
            if i >= start and data_count < page_size:
                page_data.append(item)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = i
                break

        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
