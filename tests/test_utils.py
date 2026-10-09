import unittest
from act_showcase import utils

"""
comprehensive test suite
"""


class TestUtils(unittest.TestCase):
    def test_calculate(self):
        self.assertTrue(utils.calculate(5, 3), 8)
