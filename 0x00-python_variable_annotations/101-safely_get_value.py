#!/usr/bin/env python3
"""
Module #11
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
ReturnType = Union[Any, T]
Default = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Default = None)\
        -> ReturnType:
    """11. More involved type annotations
    :param dct:
    :param key:
    :param default:
    :return:
    """
    if key in dct:
        return dct[key]
    else:
        return default
