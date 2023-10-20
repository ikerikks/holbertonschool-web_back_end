#!/usr/bin/env python3
""" simple module """


def index_range(page, page_size):
    """returns a list of page"""

    if page <= 0 or page_size <= 0:
        return (0, 0)

    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
