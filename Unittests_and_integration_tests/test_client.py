#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    # Mock get_json to return a dummy organization
    @patch('client.get_json', return_value={"login": "test-org"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        org = client.org  # Call 'org' as a property or attribute, not a method
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(org, {"login": "test-org"})

    def test_public_repos_url(self, org_name, expected_url):
        """Unit test for GithubOrgClient._public_repos_url"""
        client = GithubOrgClient("google")

        # Mock payload returned by the org property
        mock_payload = {"repos_url":expected_url}

        with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
            result = client._public_repos_url
            self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
