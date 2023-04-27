#!/usr/bin/env python3
"""
Module #11
"""
import typing

T = typing.TypeVar('T')


def safely_get_value(
        dct: typing.Mapping, key: typing.Any,
        default: typing.Union[T, None] = None) -> typing.Union[T, None]:
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
