#!/usr/bin/env python3
import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The file path to the CSV file containing the dataset.
        __dataset (List[List] or None): The cached dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server class.

        The dataset is initially set to None and will be loaded from the
        CSV file when needed.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from the CSV file if it is not already
        loaded.

        Returns:
            List[List]: The dataset, where each entry is a list of data fields
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset based on the given page number and page
        size.

        Args:
            page (int): The current page number (must be > 0).
            page_size (int): The number of items per page (must be > 0).

        Returns:
            List[List]: A list of lists containing the data for the requested
            page.

        Raises:
            AssertionError: If 'page' or 'page_size' is not an integer greater
            than 0.
        """
        assert isinstance(page, int) and page > 0, "page mustbe an int and >0"
        assert isinstance(page_size, int) and page_size > 0, "same as above!"

        start_page, end_page = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_page:end_page]
