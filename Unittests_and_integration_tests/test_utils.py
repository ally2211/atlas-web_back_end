#!/usr/bin/env python3
"""
create a unit test for utils.access_nested_map
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    '''
    method to test that the method returns what it is supposed to
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        test parameterized nested maps
        '''
        result = access_nested_map(nested_map, path)
        self. assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),                     # Test case 1: empty dictionary
        ({"a": 1}, ("a", "b"), "'b'"),           # Test case 2: key "a" exists, "b" does not
    ])
    def test_access_nested_map_exception(self, nested_map, path,  expected_message):
        """Test that access_nested_map raises KeyError with the expected message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check that the exception message matches the expected message
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase): 
    '''
        Test the get_json method by mocking requests.get
    '''
    @parameterized.expand([
    ("http://example.com", {"payload": True}),
    ("http://holberton.io", {"payload": False}),
    ])
    
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''
            test the get_json method
        '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        # call function testing
        result = get_json(test_url)
        
        # assert that requests.get was called with correct URL
        mock_get.assert_called_once_with(test_url)
        
        # assert that the returned value from the get_json is the test payload
        self.assertEqual(result, test_payload)

 
# Define TestClass outside the test function so that it can be patched
class TestClass:
    def a_method(self):
        """
        A simple method that returns 42.
        This method simulates some operation that we want to cache the result of.
        """
        return 42

    @memoize
    def a_property(self):
        """
        This method returns the result of a_method.
        Because it is decorated with @memoize, the result will be cached
        after the first call, so subsequent calls will not re-execute a_method.
        """
        return self.a_method()


class TestMemoize(unittest.TestCase):

    @patch.object(TestClass, 'a_method')  # Patch a_method of TestClass
    def test_memoize(self, mock_a_method):
        """
        Test that a_method is only called once when memoization is applied,
        even when a_property is called twice.
        """
        # Set the return value of the mock for a_method to 42
        mock_a_method.return_value = 42

        # Create an instance of TestClass
        obj = TestClass()

        # Call a_property twice
        first_call = obj.a_property
        second_call = obj.a_property

        # Assert that a_method was called once
        mock_a_method.assert_called_once()

        # Assert that both calls return the correct result
        self.assertEqual(first_call, 42)
        self.assertEqual(second_call, 42)

        # Assert that both calls return the same cached result (i.e., memoization works)
        self.assertIs(first_call, second_call)   
    
if __name__=="__main__":
    unittest.main()