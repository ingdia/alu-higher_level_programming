#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_regular_cases(self):
        """Test with normal lists of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-1]), -1)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.1, 1.2, 1.3, 1.4]), 1.4)

    def test_mixed_types(self):
        """Test with a list containing integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)
        self.assertEqual(max_integer([1.1, 2, 3.3]), 3.3)

    def test_strings(self):
        """Test with a list of strings (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
