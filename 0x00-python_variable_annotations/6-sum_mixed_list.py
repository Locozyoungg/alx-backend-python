#!/usr/bin/env python3
"""
Module for sum_mixed_list function
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of the list.
    """
    return sum(mxd_lst)


