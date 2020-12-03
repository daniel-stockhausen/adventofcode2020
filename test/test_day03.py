import unittest

from aoc.day03.day03 import count_trees_on_slope, multiply_trees_on_slopes


class TestDay03(unittest.TestCase):
    def test_03a_example(self):
        self.assertEqual(7, count_trees_on_slope('../input/day03-example.txt', (3, 1)))

    def test_03a(self):
        self.assertEqual(232, count_trees_on_slope('../input/day03.txt', (3, 1)))

    def test_03b_example(self):
        self.assertEqual(336, multiply_trees_on_slopes(
            '../input/day03-example.txt', ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))

    def test_03b(self):
        self.assertEqual(3952291680, multiply_trees_on_slopes(
            '../input/day03.txt', ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))
