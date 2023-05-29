#!/usr/bin/env python3
"""
TestGithubOrgClient
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from client import access_nested_map, get_json, memoize
from client import GithubOrgClient
from unittest import mock


class TestGithubOrgClient(unittest.TestCase):
    """Main test case class
    """

    @mock.patch('clients.get_json')
    def test_public_repos(self):
        """test"""
        # with mock.patch
        pass

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @mock.patch('clients.get_json')
    def test_org(self, org: str, response: Dict, mocked_fxn: mock.MagicMock) \
            -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = mock.MagicMock(return_value=response)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), response)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org))
