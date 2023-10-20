#!/usr/bin/env python3
""" simple pagination """

import csv
from typing import List, Dict
import math


def index_range(page, page_size):
    """returns a list of page"""

    if page <= 0 or page_size <= 0:
        return (0, 0)

    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate a database of csv file."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a list of page numbers"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)

        start, end = index_range(page, page_size)

        if start >= total_rows:
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary"""
        page_data = self.get_page(page, page_size)
        next_page_data = self.get_page(page + 1, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_dict = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if next_page_data else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }

        return hyper_dict

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
              i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert index is None or 0 <= index < len(
            self.__indexed_dataset
        ), "Index is out of range"

        if index is None:
            index = 0

        data = []
        next_index = index
        for i in range(index, index + page_size):
            if i in self.__indexed_dataset:
                data.append(self.__indexed_dataset[i])
                next_index = i + 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
