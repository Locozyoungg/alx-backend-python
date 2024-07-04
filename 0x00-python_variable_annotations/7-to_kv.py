#!/usr/bin/env python3
"""
Module for to_kv function
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string and the second element is the square of the int/float.

    Args:
    k (str): The string.
    v (Union[int, float]): The int or float.

    Returns:
    Tuple[str, float]: A tuple with the string and the square of the int/float.
    """
    return (k, float(v ** 2))
