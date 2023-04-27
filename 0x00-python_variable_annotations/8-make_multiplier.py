#!/usr/bin/env python3
"""
Module 8:
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier
    :param multiplier:
    :return:
    """
    return lambda i: i * multiplier
