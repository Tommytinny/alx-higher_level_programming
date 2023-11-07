#!/usr/bin/python3
"""
from_json_string
"""
import json


def from_json_string(my_str):
    """
    from_json_string - returns an object (python data structure)
                    represented by a JSON string:
    Args:
        my_str: json string to represent
    Return: object
    """
    return json.loads(my_str)
