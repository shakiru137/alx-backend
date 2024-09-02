#!/usr/bin/env python3
"""
This module provides a function to calculate the start and end indexes
for paginating data based on the given page number and page size.
"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index for the given
        page.
    """
    start_page = (page - 1) * page_size
    end_page = start_page + page_size
    return (start_page, end_page)
