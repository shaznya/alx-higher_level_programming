#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function."""

    def test_normal_cases(self):
        """Test with typical cases."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_mixed_types(self):
        """Test with a list containing both integers and floats."""
        self.assertEqual(max_integer([1, 2.2, 3]), 3)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1.5]), 1.5)

    def test_non_integer(self):
        """Test with a list containing non-integer types."""
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3])

if __name__ == "__main__":
    unittest.main()
