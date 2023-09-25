#!/usr/bin/env python3
'''
multiplier function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplies a number by multiplier """
    return lambda num:  num * multiplier
