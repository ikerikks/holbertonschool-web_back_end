#!/usr/bin/env python3

from typing import List, Union

"""
    sum_mixed_list function
    Args:
        mxd_list: number list
    Returns:
        sum of list
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum = 0
    for num in mxd_lst:
        sum += num
    return sum
