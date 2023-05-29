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

    @mock.patch('client.get_json')
    def test_public_repos(self, mock_get_json: mock.MagicMock) -> None:
        """test"""
        test_data = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7968417,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3OTY4NDE3",
                    "name": "dagger",
                    "full_name": "google/dagger",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                        "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/google",
                        "html_url": "https://github.com/google",
                        "followers_url": "https://api.github.com/users/google/followers",
                        "following_url": "https://api.github.com/users/google/following{/other_user}",
                        "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/google/subscriptions",
                        "organizations_url": "https://api.github.com/users/google/orgs",
                        "repos_url": "https://api.github.com/users/google/repos",
                        "events_url": "https://api.github.com/users/google/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/google/received_events",
                        "type": "Organization",
                        "site_admin": False
                    },
                    "html_url": "https://github.com/google/dagger",
                    "description": "A fast dependency injector for Android and Java.",
                    "fork": True,
                    "url": "https://api.github.com/repos/google/dagger",
                    "forks_url": "https://api.github.com/repos/google/dagger/forks",
                    "keys_url": "https://api.github.com/repos/google/dagger/keys{/key_id}",
                    "collaborators_url": "https://api.github.com/repos/google/dagger/collaborators{/collaborator}",
                    "teams_url": "https://api.github.com/repos/google/dagger/teams",
                    "hooks_url": "https://api.github.com/repos/google/dagger/hooks",
                    "issue_events_url": "https://api.github.com/repos/google/dagger/issues/events{/number}",
                    "events_url": "https://api.github.com/repos/google/dagger/events",
                    "assignees_url": "https://api.github.com/repos/google/dagger/assignees{/user}",
                    "branches_url": "https://api.github.com/repos/google/dagger/branches{/branch}",
                    "tags_url": "https://api.github.com/repos/google/dagger/tags",
                    "blobs_url": "https://api.github.com/repos/google/dagger/git/blobs{/sha}",
                    "git_tags_url": "https://api.github.com/repos/google/dagger/git/tags{/sha}",
                    "git_refs_url": "https://api.github.com/repos/google/dagger/git/refs{/sha}",
                    "trees_url": "https://api.github.com/repos/google/dagger/git/trees{/sha}",
                    "statuses_url": "https://api.github.com/repos/google/dagger/statuses/{sha}",
                    "languages_url": "https://api.github.com/repos/google/dagger/languages",
                    "stargazers_url": "https://api.github.com/repos/google/dagger/stargazers",
                    "contributors_url": "https://api.github.com/repos/google/dagger/contributors",
                    "subscribers_url": "https://api.github.com/repos/google/dagger/subscribers",
                    "subscription_url": "https://api.github.com/repos/google/dagger/subscription",
                    "commits_url": "https://api.github.com/repos/google/dagger/commits{/sha}",
                    "git_commits_url": "https://api.github.com/repos/google/dagger/git/commits{/sha}",
                    "comments_url": "https://api.github.com/repos/google/dagger/comments{/number}",
                    "issue_comment_url": "https://api.github.com/repos/google/dagger/issues/comments{/number}",
                    "contents_url": "https://api.github.com/repos/google/dagger/contents/{+path}",
                    "compare_url": "https://api.github.com/repos/google/dagger/compare/{base}...{head}",
                    "merges_url": "https://api.github.com/repos/google/dagger/merges",
                    "archive_url": "https://api.github.com/repos/google/dagger/{archive_format}{/ref}",
                    "downloads_url": "https://api.github.com/repos/google/dagger/downloads",
                    "issues_url": "https://api.github.com/repos/google/dagger/issues{/number}",
                    "pulls_url": "https://api.github.com/repos/google/dagger/pulls{/number}",
                    "milestones_url": "https://api.github.com/repos/google/dagger/milestones{/number}",
                    "notifications_url": "https://api.github.com/repos/google/dagger/notifications{?since,all,participating}",
                    "labels_url": "https://api.github.com/repos/google/dagger/labels{/name}",
                    "releases_url": "https://api.github.com/repos/google/dagger/releases{/id}",
                    "deployments_url": "https://api.github.com/repos/google/dagger/deployments",
                    "created_at": "2013-02-01T23:14:14Z",
                    "updated_at": "2019-12-03T12:39:55Z",
                    "pushed_at": "2019-11-27T21:20:38Z",
                    "git_url": "git://github.com/google/dagger.git",
                    "ssh_url": "git@github.com:google/dagger.git",
                    "clone_url": "https://github.com/google/dagger.git",
                    "svn_url": "https://github.com/google/dagger",
                    "homepage": "https://dagger.dev",
                    "size": 59129,
                    "stargazers_count": 14492,
                    "watchers_count": 14492,
                    "language": "Java",
                    "has_issues": True,
                    "has_projects": True,
                    "has_downloads": True,
                    "has_wiki": True,
                    "has_pages": True,
                    "forks_count": 1741,
                    "mirror_url": None,
                    "archived": False,
                    "disabled": False,
                    "open_issues_count": 148,
                    "license": {
                        "key": "apache-2.0",
                        "name": "Apache License 2.0",
                        "spdx_id": "Apache-2.0",
                        "url": "https://api.github.com/licenses/apache-2.0",
                        "node_id": "MDc6TGljZW5zZTI="
                    },
                    "forks": 1741,
                    "open_issues": 148,
                    "watchers": 14492,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    }
                },
                {
                    "id": 8165161,
                    "node_id": "MDEwOlJlcG9zaXRvcnk4MTY1MTYx",
                    "name": "ios-webkit-debug-proxy",
                    "full_name": "google/ios-webkit-debug-proxy",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                        "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/google",
                        "html_url": "https://github.com/google",
                        "followers_url": "https://api.github.com/users/google/followers",
                        "following_url": "https://api.github.com/users/google/following{/other_user}",
                        "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/google/subscriptions",
                        "organizations_url": "https://api.github.com/users/google/orgs",
                        "repos_url": "https://api.github.com/users/google/repos",
                        "events_url": "https://api.github.com/users/google/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/google/received_events",
                        "type": "Organization",
                        "site_admin": False
                    },
                    "html_url": "https://github.com/google/ios-webkit-debug-proxy",
                    "description": "A DevTools proxy (Chrome Remote Debugging Protocol) for iOS devices (Safari Remote Web Inspector).",
                    "fork": False,
                    "url": "https://api.github.com/repos/google/ios-webkit-debug-proxy",
                    "forks_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/forks",
                    "keys_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/keys{/key_id}",
                    "collaborators_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/collaborators{/collaborator}",
                    "teams_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/teams",
                    "hooks_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/hooks",
                    "issue_events_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues/events{/number}",
                    "events_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/events",
                    "assignees_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/assignees{/user}",
                    "branches_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/branches{/branch}",
                    "tags_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/tags",
                    "blobs_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/blobs{/sha}",
                    "git_tags_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/tags{/sha}",
                    "git_refs_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/refs{/sha}",
                    "trees_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/trees{/sha}",
                    "statuses_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/statuses/{sha}",
                    "languages_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/languages",
                    "stargazers_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/stargazers",
                    "contributors_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/contributors",
                    "subscribers_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/subscribers",
                    "subscription_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/subscription",
                    "commits_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/commits{/sha}",
                    "git_commits_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/commits{/sha}",
                    "comments_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/comments{/number}",
                    "issue_comment_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues/comments{/number}",
                    "contents_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/contents/{+path}",
                    "compare_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/compare/{base}...{head}",
                    "merges_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/merges",
                    "archive_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/{archive_format}{/ref}",
                    "downloads_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/downloads",
                    "issues_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues{/number}",
                    "pulls_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/pulls{/number}",
                    "milestones_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/milestones{/number}",
                    "notifications_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/notifications{?since,all,participating}",
                    "labels_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/labels{/name}",
                    "releases_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/releases{/id}",
                    "deployments_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/deployments",
                    "created_at": "2013-02-12T19:08:19Z",
                    "updated_at": "2019-12-04T02:06:43Z",
                    "pushed_at": "2019-11-24T07:02:13Z",
                    "git_url": "git://github.com/google/ios-webkit-debug-proxy.git",
                    "ssh_url": "git@github.com:google/ios-webkit-debug-proxy.git",
                    "clone_url": "https://github.com/google/ios-webkit-debug-proxy.git",
                    "svn_url": "https://github.com/google/ios-webkit-debug-proxy",
                    "homepage": "",
                    "size": 680,
                    "stargazers_count": 4630,
                    "watchers_count": 4630,
                    "language": "C",
                    "has_issues": True,
                    "has_projects": True,
                    "has_downloads": True,
                    "has_wiki": False,
                    "has_pages": False,
                    "forks_count": 395,
                    "mirror_url": None,
                    "archived": False,
                    "disabled": False,
                    "open_issues_count": 24,
                    "license": {
                        "key": "other",
                        "name": "Other",
                        "spdx_id": "NOASSERTION",
                        "url": None,
                        "node_id": "MDc6TGljZW5zZTA="
                    },
                    "forks": 395,
                    "open_issues": 24,
                    "watchers": 4630,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    }
                },
            ]
        }
        mock_get_json.return_value = test_data["repos"]
        with mock.patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=mock.PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_data["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                ['dagger', 'ios-webkit-debug-proxy'],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @mock.patch('client.get_json')
    def test_org(self, org: str, resp: Dict, mocked_fxn: mock.MagicMock) \
            -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = mock.MagicMock(return_value=resp)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org))

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property of the class"""
        with mock.patch("client.GithubOrgClient.org",
                        new_callable=mock.PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"}
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos")
