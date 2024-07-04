#!/usr/bin/env python3
"""
Module for zoom_array function
"""
from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a zoomed-in version of the array by repeating each element 'factor' times.

    Args:
    lst (Tuple[int, ...]): The input tuple.
    factor (int): The factor by which to zoom in.

    Returns:
    List[int]: The zoomed-in list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)


