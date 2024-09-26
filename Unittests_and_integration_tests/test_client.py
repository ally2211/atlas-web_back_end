#!/usr/bin/env python3
import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Unit test for GithubOrgClient.public_repos"""
        # Sample payload for the mock get_json to return
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Mocked URL that _public_repos_url should return
        mocked_repos_url = "https://api.github.com/orgs/google/repos"

        client = GithubOrgClient("google")

        # Use patch as a context manager to mock _public_repos_url
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value=mocked_repos_url):
            repos = client.public_repos()  # Call the public_repos method

            # Assertions for expected repos list
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)

            # Verify mocked property and get_json were called exactly once
            mock_get_json.assert_called_once_with(mocked_repos_url)

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

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos")
    ])
    def test_public_repos_url(self, org_name, expected_url):
        """Unit test for GithubOrgClient._public_repos_url
        using parameterized inputs
        """
        client = GithubOrgClient(org_name)

        # Mock payload returned by the org property
        mock_payload = {"repos_url": expected_url}

        # Patch the 'org' property to return mock payload using PropertyMock
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock,
                          return_value=mock_payload):
            result = client._public_repos_url
            self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
