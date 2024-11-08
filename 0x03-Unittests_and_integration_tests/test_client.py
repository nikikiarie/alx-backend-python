#!/usr/bin/env python3
""" Module for testing client """

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ Class for Testing Github Org Client """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input_org, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client_instance = GithubOrgClient(input_org)
        client_instance.org()
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{input_org}')

    def test_public_repos_url(self):
        """ Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            org_payload = {"repos_url": "World"}
            mock_org.return_value = org_payload
            client_instance = GithubOrgClient('test')
            result = client_instance._public_repos_url
            self.assertEqual(result, org_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        repo_json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = repo_json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_url:

            mock_public_url.return_value = "hello/world"
            client_instance = GithubOrgClient('test')
            result = client_instance.public_repos()

            check = [i["name"] for i in repo_json_payload]
            self.assertEqual(result, check)

            mock_public_url.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo_data, license_key, expected_result):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo_data, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(
    ("org_data", "repos_data", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """A class method called before tests in an individual class are run"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_data, cls.repos_data,
                      cls.org_data, cls.repos_data
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock_request = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test: public repos"""
        client_instance = GithubOrgClient("google")

        self.assertEqual(client_instance.org, self.org_data)
        self.assertEqual(client_instance.repos_data, self.repos_data)
        self.assertEqual(client_instance.public_repos(), self.expected_repos)
        self.assertEqual(client_instance.public_repos("XLICENSE"), [])
        self.mock_request.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        client_instance = GithubOrgClient("google")

        self.assertEqual(client_instance.public_repos(), self.expected_repos)
        self.assertEqual(client_instance.public_repos("XLICENSE"), [])
        self.assertEqual(client_instance.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock_request.assert_called()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop()
