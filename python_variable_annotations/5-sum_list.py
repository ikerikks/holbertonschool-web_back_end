#!/usr/bin/env python3

from typing import List

"""
    sum_list function
    Args:
        input_list: list of float numbers
    Returns:
        sum of lists
"""


def sum_list(input_list: List[float]) -> float:
    sum: float = 0
    for num in input_list:
        sum += num
    return float(sum)
