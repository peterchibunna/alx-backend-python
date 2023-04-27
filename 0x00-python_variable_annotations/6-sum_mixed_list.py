#!/usr/bin/env python3
"""
Module #6
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns the floating point sum of items in a list
    :param mxd_lst:
    :return:
    """
    return float(sum(mxd_lst))
