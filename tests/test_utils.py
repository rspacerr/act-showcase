import unittest
from act_showcase import utils

"""
comprehensive test suite
"""


class TestUtils(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(utils.calculate(5, 3), 8)

    def test_calculate2(self):
        self.assertEqual(utils.calculate2(utils.calculate(5, 3), 5), 3)
