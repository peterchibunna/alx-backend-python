#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json, memoize
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
    def test_get_json(self, test_url, expected):
        """2. Mock HTTP calls
        """
        with mock.patch('requests.get', return_value=mock.Mock(
                **{'json.return_value': expected})) as patched_req_get:
            self.assertEqual(get_json(test_url), expected)
            patched_req_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Class implementation as required
    """

    def test_memoize(self):
        """3. Parameterize and patch
        """

        class TestClass:
            """Inner class
            """

            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """a property"""
                return self.a_method()

        with mock.patch.object(TestClass, "a_method",
                               return_value=lambda: 42) as memo_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_method.assert_called_once()
