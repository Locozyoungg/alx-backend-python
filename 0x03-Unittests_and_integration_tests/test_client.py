#!/usr/bin/env python3
""" Test the utils """

import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
import utils
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Test that json can be got """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, expected: dict, get_patch: Mock) -> None:
        """ Test the org of the client """
        get_patch.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/" + org)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock: Mock) -> None:
        """ Test the public repos """
        # Define the mock data
        repos_payload = [
            {"name": "Repo1", "license": {"key": "a"}},
            {"name": "Repo2", "license": {"key": "b"}},
            {"name": "Repo3", "license": {"key": "a"}}
        ]
        expected_url = "https://api.github.com/orgs/x/repos"
        get_json_mock.return_value = repos_payload

        # Patch _public_repos_url
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = expected_url
            
            # Instantiate the client
            client = GithubOrgClient("x")
            
            # Test public_repos method
            self.assertEqual(client.public_repos(), ['Repo1', 'Repo2', 'Repo3'])
            self.assertEqual(client.public_repos("a"), ['Repo1', 'Repo3'])
            self.assertEqual(client.public_repos("b"), ['Repo2'])
            self.assertEqual(client.public_repos("c"), [])
            
            # Check if the mocks were called as expected
            get_json_mock.assert_called_once_with(expected_url)
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: dict, license_key: str, expected: bool) -> None:
        """ Test the license checker """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for github org client """

    @classmethod
    def setUpClass(cls) -> None:
        """ Prepare for testing """
        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        # Set up the mock responses
        cls._mock_responses = {
            cls.org_payload["repos_url"]: cls.repos_payload,
            "https://api.github.com/orgs/x": cls.org_payload
        }

        cls.get.side_effect = lambda url: Mock(json=Mock(return_value=cls._mock_responses.get(url, {})))

    @classmethod
    def tearDownClass(cls) -> None:
        """ Unprepare for testing """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """ Public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self) -> None:
        """ Public repos test with license filter """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

