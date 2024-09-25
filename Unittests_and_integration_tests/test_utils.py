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

if __name__=="__main__":
    unittest.main()