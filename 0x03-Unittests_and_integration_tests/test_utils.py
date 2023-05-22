#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json
import unittest.mock as mock


class TestAccessNestedMap(unittest.TestCase):
    """The main testcase class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """Implement the named method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Implement this test: 1. Parameterize a unit test
        """
        with self.assertRaises(expected_exception=expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json class
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, expected):
        """2. Mock HTTP calls
        """
        with mock.patch('requests.get', data=mock.Mock(
                **{'json.return_value': expected})) as get:
            self.assertEqual(get_json(url), expected)
            get.assert_called_once(url)
