"""System module"""
import unittest
import numpy as np

from src import Polynomial


class PolynomialTest(unittest.TestCase):
    '''
    Polynomial test
    '''
    def test_square_of_three_should_be_nine(self):
        """function for polynomial test"""
        # given
        polynom = Polynomial(np.array([1, 0, 0]))
        x_value = 3
        expected = 9
        # when
        actual = polynom.evaluate(x_value)
        # then
        self.assertEqual(expected, actual)
