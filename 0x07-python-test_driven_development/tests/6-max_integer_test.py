#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):

        maxx = max_integer([20, 98, 67, 90])
        maxx2 = max_integer([-1, -89, -1000, 0])
        maxx3 = max_integer([1])
        max4 = max_integer([1000, 200, 19])

        self.assertEqual(maxx2, 0)
        self.assertEqual(maxx, 98)
        self.assertEqual(maxx3, 1)
        self.assertEqual(max4, 1000)

    def test_Elist(self):

        result = max_integer([])

        self.assertEqual(result, None)
        self.assertRaises(TypeError, max_integer())

    def test_type(self):

        self.assertRaises(TypeError, max_integer(["me", "7"]))
        self.assertRaises(TypeError, max_integer("hi"))
