#!/usr/bin/env python3
"""
Module #9:
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) \
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    returns the element's length as expected
    :param lst:
    :return:
    """
    return [(i, len(i)) for i in lst]
