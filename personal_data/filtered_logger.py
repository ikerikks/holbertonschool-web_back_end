#!/usr/bin/env python3
"""
logger module
"""
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    pattern = re.compile(rf'({"|".join(fields)})=[^{separator}]+')
    return re.sub(pattern, rf"\1={redaction}", message)
