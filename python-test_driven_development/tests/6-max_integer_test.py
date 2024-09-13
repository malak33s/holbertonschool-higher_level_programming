#!/usr/bin/python3
"""unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""
    def test_the_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([4]), 4)

    def test_negative_number(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_string(self):
        self.assertEqual(max_integer(["python"]), "python")

    def test_same_number(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_middle_list(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)
