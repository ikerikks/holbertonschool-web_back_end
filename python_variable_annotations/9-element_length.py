#!/usr/bin/env python3
'''
length function
'''
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ list of elements length """
    return [(i, len(i)) for i in lst]
