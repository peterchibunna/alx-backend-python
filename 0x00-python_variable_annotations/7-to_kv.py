#!/usr/bin/env python3
"""
Module #7:
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    returns a tuple of k and v^2
    :param k:
    :param v:
    :return:
    """
    return str(k), float(v ** 2)
