#!/usr/bin/env python3

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum of the list """
    sum: float = 0
    for num in input_list:
        sum += num
    return float(sum)
