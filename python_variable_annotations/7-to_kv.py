#!/usr/bin/env python3

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ list of botth arguments values"""
    return (k, v * v)
