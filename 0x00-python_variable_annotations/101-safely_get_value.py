#!/usr/bin/env python3
"""
Module for safely_get_value function
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value for the key in the dictionary if it exists, otherwise returns the default value.

    Args:
    dct (Mapping[Any, Any]): The dictionary.
    key (Any): The key to lookup.
    default (Union[T, None]): The default value to return if key does not exist.

    Returns:
    Union[Any, T]: The value for the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

