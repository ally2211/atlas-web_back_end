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
    @patch('client.get_json', return_value={"login": "test-org"})  # Mock get_json to return a dummy organization
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        org = client.org  # Call 'org' as a property or attribute, not a method
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(org, {"login": "test-org"})


if __name__ == '__main__':
    unittest.main()
