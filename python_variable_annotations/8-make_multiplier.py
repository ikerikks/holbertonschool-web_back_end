#!/usr/bin/env python3

from typing import Callable

"""
    make_multiplier fuction
    Args:
        multiplier: number
    Returns:
        function that multiplies a number by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
        return lambda num:  num * multiplier
