#!/usr/bin/env python3

from typing import List, Tuple, Iterable, Sequence

"""
    element_length function
    Args:
        lst: list
    Returns:
        list of elements length
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
