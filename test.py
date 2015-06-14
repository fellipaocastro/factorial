#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
import unittest
import math
import random

from factorial import factorial


class FactorialTestCase(unittest.TestCase):
    def test_factorial_of_0_should_return_1(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_3_should_return_6(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_should_return_the_same_value_as_math_factorial(self):
        n = random.randint(0, 100)

        self.assertEqual(factorial(n), math.factorial(n))

if __name__ == '__main__':
    unittest.main()
