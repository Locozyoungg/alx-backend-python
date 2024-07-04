#!/usr/bin/env python3
"""
Module for safely_get_value function
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Returns the value for the key in the dictionary if it exists, otherwise returns the default value.

    Args:
    dct (Mapping[Any, T]): The dictionary.
    key (Any): The key to lookup.
    default (Union[T, None]): The default value to return if key does not exist.

    Returns:
    Union[T, None]: The value for the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

