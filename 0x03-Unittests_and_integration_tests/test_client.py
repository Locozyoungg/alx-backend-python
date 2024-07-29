#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"name": "mocked_org"})
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"name": "mocked_org"})

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos")
    ])
    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, org_name, expected_url, mock_org):
        # Define the mock payload
        mock_org.return_value = {
            'repos_url': expected_url
        }
        
        # Instantiate the client
        client = GithubOrgClient(org_name)
        
        # Call the method
        result = client._public_repos_url
        
        # Assert the result
        self.assertEqual(result, expected_url)

if __name__ == '__main__':
    unittest.main()
