#!/usr/bin/env python3
"""
create a unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    method to test that the method returns what it is supposed to
    '''      
    @parameterized.expand([
        ({}, ("a",)),                     # Test case 1: empty dictionary
        ({"a": 1}, ("a", "b")),           # Test case 2: key "a" exists, "b" does not
    ])
        
    def test_access_nested_map_key_error(self, nested_map, path):
        """Test that access_nested_map raises KeyError for invalid keys."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__=="__main__":
    unittest.main()