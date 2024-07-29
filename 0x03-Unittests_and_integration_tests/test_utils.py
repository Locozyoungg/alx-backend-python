#!/usr/bin/env python3
"""
utils.py

This module contains utility functions for accessing nested maps.
"""

from typing import Any, Dict, Tuple

def access_nested_map(nested_map: Dict[str, Any], path: Tuple[str, ...]) -> Any:
    """
    Access a nested map with a given path.

    Args:
        nested_map (Dict[str, Any]): The dictionary to access.
        path (Tuple[str, ...]): The path of keys to access in the dictionary.

    Returns:
        Any: The value found at the end of the path in the nested dictionary.

    Raises:
        KeyError: If a key in the path does not exist in the dictionary.
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map
