#!/usr/bin/env python3
"""
Module #10:
"""
import typing


# The types of the elements of the input are not known


def safe_first_element(lst: typing.Sequence[typing.Any])\
        -> typing.Union[typing.Any, None]:
    """
    Augment the following code with the correct duck-typed annotations:
    :param lst:
    :return:
    """
    if lst:
        return lst[0]
    else:
        return None
