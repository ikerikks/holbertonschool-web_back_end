#!/usr/bin/env python3

from typing import Union, Tuple

"""
    to_kv function
    Args:
        k: string
        v: number
    Returns:
        a list with both parameters values
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v * v)
