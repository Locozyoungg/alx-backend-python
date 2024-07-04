#!/usr/bin/env python3
"""
Module for make_multiplier function
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func


