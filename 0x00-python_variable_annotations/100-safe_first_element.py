#!/usr/bin/env python3
"""
Module for safe_first_element function
"""
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, otherwise None.

    Args:
    lst (Sequence[Any]): A sequence of any type.

    Returns:
    Union[Any, None]: The first element or None.
    """
    if lst:
        return lst[0]
    else:
        return None


