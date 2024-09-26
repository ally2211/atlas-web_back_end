#!/usr/bin/env python3
"""
create a unit test for client
"""
import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


@parameterized_class([
    {
        "org_payload": fixtures.TEST_PAYLOAD[0][0],
        "repos_payload": fixtures.TEST_PAYLOAD[0][1],
        "expected_repos": ["episodes.dart", "another_repo"],
        "apache2_repos": ["episodes.dart"] 
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up the class with the necessary patching and fixtures"""
        # Start patching 'requests.get' with a mock
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side effects for 'requests.get' based on the URL called
        def get_side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return MockResponse(cls.org_payload)  # Return org_payload mock
            elif url == cls.org_payload["repos_url"]:
                return MockResponse(cls.repos_payload)  # Return repos_payload mock
            return None

        cls.mock_get.side_effect = get_side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patching 'requests.get'"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the correct list of repositories"""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtering repos by Apache 2.0 license"""
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)

class MockResponse:
    """Mock response class to simulate requests.get().json()"""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        # Repo has my_license
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        # Repo has other_license, looking for my_license
        ({"license": {"key": "other_license"}}, "other_license", True),
        # Repo has other_license
        ({"license": None}, "my_license", False),
        # No license key, looking for my_license
        ({}, "my_license", False)
        # No license information
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Unit test for GithubOrgClient.has_license,
        parameterized with multiple cases
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

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
